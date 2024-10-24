from concurrent.futures import ThreadPoolExecutor
from Separated.Weather_separate import get_current_weather
from Repositories.Weather_repository import *
from config import settings
import asyncio
import argparse
import pandas as pd


def save_to_excel(df, output_file):
    try:
        df.to_excel(output_file, index=False, engine='openpyxl')  # export data to excel
        print(f'Данные успешно экспортированы в {output_file}')
    except Exception as ex:
        print(ex)


async def convert_to_xlsx(output_file):
    query = await query_weather()  # get all weather data from DB
    # converting DB data to DF type
    df = pd.DataFrame(query,
                      columns=['time', 'temperature', 'direction', 'speed', 'pressure', 'precipitation', 'precip_type'])
    # create a thread pool for parallel export execution
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, save_to_excel, df, output_file)


async def action_weather():
    while True:
        # getting specific weather data
        data = await get_current_weather(api_url=settings.api_url, apikey=settings.apikey, location='Moscow')
        if not data:
            break
        await asyncio.create_task(add_weather(data))  # writing weather data to the database
        await asyncio.sleep(60 * 60)


async def main(out_file: str):
    print("To stop parsing, press Ctrl+C")
    await create_tables()  # create all tables in DB
    async with asyncio.TaskGroup() as tg:
        tg.create_task(action_weather())
        tg.create_task(convert_to_xlsx(output_file=out_file))


if __name__ == '__main__':
    # added arguments for cmd
    parse_obj = argparse.ArgumentParser(description="Export data to .xlsx")
    parse_obj.add_argument('out_file', type=str, help='path to export file (.xlsx)')
    args = parse_obj.parse_args()
    # launch coroutines
    asyncio.run(main(args.out_file))

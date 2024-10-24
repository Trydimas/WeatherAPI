from database import Session
from Schemes.Weather_schemes import WeatherCurrent
from Models.Weather_models import WeatherTbl
from database import Base, engine
from sqlalchemy import select


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_weather(weather_data: WeatherCurrent):
    async with Session.begin() as session:
        session.add(WeatherTbl(**weather_data))
        await session.commit()


async def query_weather():
    async with Session() as session:
        query = select(WeatherTbl.time,
                       WeatherTbl.temperature,
                       WeatherTbl.direction,
                       WeatherTbl.speed,
                       WeatherTbl.pressure,
                       WeatherTbl.precipitation,
                       WeatherTbl.precip_type)
        res = await session.execute(query)
        return res.fetchall()

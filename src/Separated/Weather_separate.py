from Requests.HttpClient import ApiWeather
from datetime import datetime


def convert_wind_direction(w_dir: float):
    directions = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest"]
    return directions[round(w_dir / 45.0) % 8]


async def get_current_weather(api_url, apikey, location):
    weather = ApiWeather(api_url=api_url, apikey=apikey, location=location)
    data = await weather.get_all_weather()  # unfiltered data
    # if data from the server has not been received
    if not data:
        return data
    currency_data = data['locations'][location]['values'][0]  # current weather data
    time = datetime.fromisoformat(currency_data['datetimeStr']).replace(
        tzinfo=None)  # datetimeStr UTC -> datetime without timezone
    temperature = currency_data['temp']  # degrees Celsius
    wind_direction = convert_wind_direction(currency_data['wdir'])  # direction angle in names
    wind_speed = round(currency_data['wspd'] / 3.6, 3)  # km/h -> m/s
    air_pressure = currency_data['sealevelpressure'] * 0.7501  # mb -> ~mmHg.
    precip = currency_data['precip']
    precip_type = currency_data['conditions']
    return {
        "time": time,
        "temperature": temperature,
        "direction": wind_direction,
        "speed": wind_speed,
        "pressure": air_pressure,
        "precipitation": precip,
        "precip_type": precip_type
    }

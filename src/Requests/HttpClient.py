from config import settings
import aiohttp


class ApiWeather:
    def __init__(self, api_url, apikey, location):
        self.api_url = api_url
        self.apikey = apikey
        self.location = location

    async def get_all_weather(self):
        param = {
            "locations": self.location,
            "key": self.apikey,
            "contentType": "json",
            "shortColumnNames": "false",
            "aggregateHours": "1",
            "forecastDays": "1",
            "unitGroup": "metric",
            "include": "current"
        }
        try:
            # https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast
            async with aiohttp.ClientSession(base_url=settings.api_url) as session:
                async with session.get(
                        url=f'/VisualCrossingWebServices/rest/services/weatherdata/forecast',
                        params=param
                ) as response:
                    return await response.json()
        except Exception as ex:
            print(ex)
            return None

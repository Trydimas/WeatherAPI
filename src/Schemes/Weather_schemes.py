from pydantic import BaseModel
from datetime import datetime


class WeatherCurrent(BaseModel):
    time: datetime
    temperature: float
    direction: str
    speed: float
    pressure: float
    precipitation: float
    precip_type: str

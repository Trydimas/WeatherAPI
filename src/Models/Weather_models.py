from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, text
from datetime import datetime
from database import Base


class WeatherTbl(Base):
    __tablename__ = "Weather"
    id: Mapped[int] = mapped_column(primary_key=True)
    time: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    temperature: Mapped[float]
    direction: Mapped[str]
    speed: Mapped[float]
    pressure: Mapped[float]
    precipitation: Mapped[float]
    precip_type: Mapped[str]

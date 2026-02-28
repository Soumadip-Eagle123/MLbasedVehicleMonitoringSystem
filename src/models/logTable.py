from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from datetime import datetime
from src.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    engine_temperature = Column(Float)
    rpm = Column(Float)
    battery_voltage = Column(Float)
    tire_pressure = Column(Float)
    vibration = Column(String)

    health_score = Column(Float)
    ml_prediction = Column(String)
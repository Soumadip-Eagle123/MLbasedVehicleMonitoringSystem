from pydantic import BaseModel
from datetime import datetime

class SimulationResponse(BaseModel):
    engine_temperature: float
    rpm: float
    battery_voltage: float
    tire_pressure: float
    vibration: str
    health_score: float
    ml_prediction: str
    timestamp: datetime


class DailyAverageResponse(BaseModel):
    date: str
    avg_health: float
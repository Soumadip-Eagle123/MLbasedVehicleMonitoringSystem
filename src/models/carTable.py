from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from src.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    car_model = Column(String)
    manufacturing_year = Column(Integer)
    total_mileage = Column(Integer)

    age_years = Column(Integer)
    fuel_type_code = Column(Integer)
    service_history_code = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
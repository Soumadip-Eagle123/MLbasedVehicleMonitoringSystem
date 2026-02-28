from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from src.database import SessionLocal
from src.models.carTable import Car
from src.models.logTable import Log
from src.schemas.mlSchemas import MLResponse
from src.ml_model.predictor import VehicleHealthSystem

router = APIRouter(prefix="/simulation", tags=["Simulation"])
ml_system = VehicleHealthSystem()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{car_id}", response_model=MLResponse)
def simulate(car_id: int, db: Session = Depends(get_db)):

    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    sensor_data = {
        "engine_temperature_c": random.uniform(70, 120),
        "rpm": random.uniform(700, 5000),
        "battery_voltage": random.uniform(11.5, 13.8),
        "tire_pressure_psi": random.uniform(28, 36),
        "vibration_mm_per_s": random.uniform(0, 8),
    }

    full_input = {
        "age_years": car.age_years,
        "fuel_type": car.fuel_type_code,
        "mileage_km": car.total_mileage,
        "service_history": car.service_history_code,
        **sensor_data
    }

    result = ml_system.predict(full_input)

    log = Log(
        car_id=car_id,
        health_score=result["health_score"],
        ml_prediction=result["risk_level"]
    )

    db.add(log)
    db.commit()

    return result
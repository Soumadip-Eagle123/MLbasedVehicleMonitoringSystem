from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from src.database import SessionLocal
from src.models.carTable import Car
from src.schemas.carSchema import CarCreate

router = APIRouter(prefix="/cars", tags=["Cars"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_car(user_id: int, car: CarCreate, db: Session = Depends(get_db)):

    current_year = datetime.utcnow().year
    age_years = current_year - car.manufacturing_year

    new_car = Car(
        user_id=user_id,
        car_model=car.car_model,
        manufacturing_year=car.manufacturing_year,
        total_mileage=car.total_mileage,
        age_years=age_years,
        fuel_type_code=car.fuel_type,
        service_history_code=car.service_history
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


@router.get("/")
def get_cars(user_id: int, db: Session = Depends(get_db)):

    cars = db.query(Car).filter(Car.user_id == user_id).all()

    return [
        {
            "id": car.id,
            "car_model": car.car_model,
            "manufacturing_year": car.manufacturing_year,
            "total_mileage": car.total_mileage,
            "fuel_type": car.fuel_type_code,
            "service_history": car.service_history_code
        }
        for car in cars
    ]
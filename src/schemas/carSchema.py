from pydantic import BaseModel, Field

class CarCreate(BaseModel):
    car_model: str = Field(..., min_length=2, max_length=50)
    manufacturing_year: int = Field(..., ge=1990, le=2026)

    total_mileage: int = Field(..., ge=0, le=300000)

    # these are integer codes (0,1,2)
    fuel_type: int = Field(..., ge=0, le=2)
    service_history: int = Field(..., ge=0, le=2)
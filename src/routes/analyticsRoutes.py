from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from collections import defaultdict

from src.database import SessionLocal
from src.models.logTable import Log
from src.schemas.logSchema import DailyAverageResponse

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{car_id}/last7days", response_model=list[DailyAverageResponse])
def last7days(car_id: int, db: Session = Depends(get_db)):

    seven_days_ago = datetime.utcnow() - timedelta(days=7)

    logs = db.query(Log).filter(
        Log.car_id == car_id,
        Log.timestamp >= seven_days_ago
    ).all()

    grouped = defaultdict(list)

    for log in logs:
        date_key = log.timestamp.date().isoformat()
        grouped[date_key].append(log.health_score)

    result = []

    for date, scores in grouped.items():
        avg = sum(scores) / len(scores)
        result.append(DailyAverageResponse(
            date=date,
            avg_health=avg
        ))

    return result
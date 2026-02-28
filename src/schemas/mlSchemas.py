from pydantic import BaseModel
from typing import List


class MLResponse(BaseModel):
    health_score: float
    risk_level: str
    anomaly_detected: bool
    top_issues: List[str]
    recommendations: List[str]
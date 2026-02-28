FEATURE_COLUMNS = [
    "age_years",
    "fuel_type",
    "mileage_km",
    "service_history",
    "engine_temperature_c",
    "rpm",
    "battery_voltage",
    "tire_pressure_psi",
    "vibration_mm_per_s"
]

TARGET_COLUMN = "score"

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCORE_MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "score_model.pkl")
ANOMALY_MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "anomaly_model.pkl")
DATA_PATH = os.path.join(os.path.dirname(BASE_DIR), "dataset", "generated_data_with_score.csv")

#DATA_PATH = "dataset/generated_data_with_score.csv"
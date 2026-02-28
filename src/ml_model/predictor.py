import joblib
import pandas as pd
import numpy as np

from .config import *
from .recommender import generate_recommendations


class VehicleHealthSystem:

    def __init__(self):
        self.score_model = joblib.load(SCORE_MODEL_PATH)
        self.anomaly_model = joblib.load(ANOMALY_MODEL_PATH)

    def classify_risk(self, score):
        if score >= 70:
            return "Healthy"
        elif score >= 40:
            return "Warning"
        else:
            return "Critical"

    def get_top_features(self):

        preprocessor = self.score_model.named_steps["preprocessor"]
        model = self.score_model.named_steps["model"]

        feature_names = preprocessor.get_feature_names_out()
        importances = model.feature_importances_

        indices = np.argsort(importances)[::-1][:2]
        top_features_raw = [feature_names[i] for i in indices]

        readable_map = {
            "num__age_years": "High vehicle age",
            "num__mileage_km": "High mileage",
            "num__engine_temperature_c": "Engine temperature deviation",
            "num__rpm": "RPM instability",
            "num__battery_voltage": "Battery voltage issue",
            "num__tire_pressure_psi": "Improper tire pressure",
            "num__vibration_mm_per_s": "High vibration",
            "cat__fuel_type_0": "Fuel type: Petrol",
            "cat__fuel_type_1": "Fuel type: Diesel",
            "cat__fuel_type_2": "Fuel type: Electric",
            "cat__service_history_0": "Service history: Regular",
            "cat__service_history_1": "Service history: Occasional",
            "cat__service_history_2": "Service history: Poor"
        }

        top_features = [readable_map.get(f, f) for f in top_features_raw]

        return top_features

    def predict(self, input_data: dict):

        df = pd.DataFrame([input_data])

        health_score = float(self.score_model.predict(df)[0])

        anomaly_flag = self.anomaly_model.predict(df)[0]
        anomaly_detected = True if anomaly_flag == -1 else False

        risk_level = self.classify_risk(health_score)

        top_issues = self.get_top_features()

        recommendations = generate_recommendations(input_data)

        return {
            "health_score": round(health_score, 2),
            "risk_level": risk_level,
            "anomaly_detected": anomaly_detected,
            "top_issues": top_issues,
            "recommendations": recommendations
        }
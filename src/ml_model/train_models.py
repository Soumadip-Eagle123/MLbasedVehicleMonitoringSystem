import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

from .config import *

def train_models():

    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    print("Training Score Model...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    
    categorical_cols = ["fuel_type", "service_history"]
    numerical_cols = [
        "age_years",
        "mileage_km",
        "engine_temperature_c",
        "rpm",
        "battery_voltage",
        "tire_pressure_psi",
        "vibration_mm_per_s"
    ]
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
        ]
    )
    
    score_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=400,
            max_depth=None,
            random_state=42
        ))
    ])

    score_pipeline.fit(X_train, y_train)

    y_pred = score_pipeline.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"Score Model R2: {r2:.4f}")
    print(f"Score Model RMSE: {rmse:.4f}")

    joblib.dump(score_pipeline, SCORE_MODEL_PATH)

    print("Training Anomaly Model...")

    anomaly_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", IsolationForest(
            n_estimators=200,
            contamination=0.05,
            random_state=42
        ))
    ])

    anomaly_pipeline.fit(X)

    joblib.dump(anomaly_pipeline, ANOMALY_MODEL_PATH)

    print("Models saved successfully!")


if __name__ == "__main__":
    train_models()
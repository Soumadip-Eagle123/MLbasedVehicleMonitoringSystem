# 🔹 ML-Based Vehicle Health Monitoring System

Modern vehicles generate a lot of data — engine temperature, RPM, battery voltage, vibration levels, mileage history, and more.  
But raw numbers alone don’t really help someone understand the condition of their vehicle.

This project was built to bridge that gap.

The **ML-Based Vehicle Health Monitoring System** is a full-stack intelligent platform that predicts vehicle health, detects abnormal behavior, and provides actionable maintenance recommendations using Machine Learning.

Instead of just showing metrics, the system translates data into insights that actually make sense.

---

## 🔹 Overview

This system allows users to:

- Register and manage their vehicles
- Simulate live vehicle sensor data
- Predict a vehicle health score (0–100)
- Detect abnormal vehicle behavior
- View analytics trends over time
- Receive practical maintenance recommendations

The system combines:

- React Frontend
- FastAPI Backend
- Machine Learning Pipeline
- Supabase (PostgreSQL Cloud Database)

---

![Dashboard](assets/dashboard.png)

---

# 🔹 System Architecture

```
Frontend (React)
        ↓
FastAPI Backend
        ↓
ML Models + Recommendation Engine
        ↓
Supabase PostgreSQL
```
The frontend focuses on user experience and visualization.  
The backend handles authentication, API routing, and database interaction.  
The ML models perform prediction and anomaly detection.  
Supabase securely stores all user and vehicle data.
---

# 🔹 Running the Project Locally

If you'd like to run this project on your own system, follow the steps below.

## 1️Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd vehicle-health-system
```

---

## 2️Backend Setup (FastAPI)

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File

Create a `.env` file in root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
```

> This project uses Supabase as a hosted PostgreSQL database.

---

### Start Backend Server

```bash
uvicorn src.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```
![Swagger docs(deployed)](assets/swagger_docs.jpeg)

---

## 3️Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🔹 How to Use the Website

### 1️Register / Login  
Create an account and log in to access your dashboard.

### 2️Add Vehicle  
Provide the following details:
- Model
- Manufacturing year
- Mileage
- Fuel type
- Service history
These details are used to calculate vehicle age and form the base input for prediction.
### 3️Monitor Vehicle  
On the monitoring page, simulated live sensor data is generated and passed into the ML pipeline.

The system will:
- Predict a health score
- Classify the risk level (Healthy / Warning / Critical)
- Detect anomalies
- Generate recommendations
---

![Health Simulation](assets/simulation.png)

---

### 4️View Analytics  
The analytics page provides:
- 7-Day Health Average
- Health trend visualization
- Historical performance tracking
This helps understand how the vehicle’s condition evolves over time.

---

![Analytics Page](assets/analytics.png)

---

# 🔹 Machine Learning Module

This repository includes the Machine Learning module that powers the intelligence behind the system.

The ML system predicts overall vehicle health using structured sensor and historical data, detects abnormal behavior patterns, and generates practical recommendations.

The design intentionally combines multiple approaches instead of relying on a single model.

---

## 🔹 Hybrid Intelligent Pipeline

```
Input Features
      ↓
Health Score Model (Supervised)
      ↓
Risk Classification
      ↓
Anomaly Detection Model (Unsupervised)
      ↓
Feature Importance
      ↓
Rule-Based Recommendation Engine
```
Two trained models form the core of the system:

1. **Health Score Model** (Random Forest Regressor)  
2. **Anomaly Detection Model** (Isolation Forest)

The final output is not just a number — it includes classification, anomaly flagging, and suggestions.

---

## 🔹 Input Features

| Feature              | Type  | Description                     |
| -------------------- | ----- | ------------------------------- |
| age_years            | int   | Age of vehicle                  |
| fuel_type            | int   | 0=Petrol, 1=Diesel, 2=Electric  |
| mileage_km           | int   | Total mileage                   |
| service_history      | int   | 0=Regular, 1=Occasional, 2=Poor |
| engine_temperature_c | float | Engine temperature in °C        |
| rpm                  | float | Engine RPM                      |
| battery_voltage      | float | Battery voltage                 |
| tire_pressure_psi    | float | Tire pressure                   |
| vibration_mm_per_s   | float | Engine vibration                |

---

# 🔹 Health Score Model

**Model Type:** `RandomForestRegressor` (scikit-learn)

**Output:** The model outputs a health score between 0 and 100.

| Score Range | Status     |
|------------|------------|
| 70–100     | Healthy    |
| 40–69      | Warning    |
| 0–39       | Critical   |

The model was trained on a synthetic dataset generated using realistic automotive constraints to simulate real-world vehicle behavior.

### 🔹 Performance

- **R² Score ≈ 0.85**
- **RMSE ≈ 4.6**
These metrics indicate strong predictive capability with low error variance.
---

![ML Training Output](assets/ml_training.png)

---

# 🔹 Anomaly Detection Model

**Model Type:** `IsolationForest`

While the health score measures degradation trends, anomaly detection focuses on unusual sensor behavior.

For example:

A vehicle may have a moderate health score but exhibit abnormal vibration patterns — this would be flagged as an anomaly.

The contamination parameter is calibrated at approximately 8% to balance sensitivity and noise reduction.

---

# 🔹 Recommendation Engine

Prediction alone is not enough.

A rule-based system converts sensor deviations into actionable maintenance suggestions.

Examples:

- High engine temperature → Inspect cooling system
- Low battery voltage → Check battery health
- Poor service history → Immediate servicing required

This ensures the system provides practical guidance rather than just analytics.

---

# 🔹 Database Layer

Database: **Supabase PostgreSQL**

Tables:

- users
- cars
- logs

SQLAlchemy is used as the ORM layer to manage database interactions.

---

![Supabase Tables](assets/supabase_tables.png)

---

# 🔹 Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Chart.js

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Machine Learning
- scikit-learn
- RandomForestRegressor
- IsolationForest
- NumPy / Pandas

### Database
- Supabase (PostgreSQL)

---

# 🔹 Future Improvements

 - Integration with real IoT sensor streams

 - Real-time data ingestion

 - Predictive maintenance scheduling

 - Cloud deployment (Render / Railway / AWS)

 - Real-time anomaly alerts

---

# 🔹 Contributors

- ML Module: Priyanshu Jangid
- Full Stack & Integration: Soumadip and Abhinav

---

# 🔹 License

MIT License
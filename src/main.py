from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import engine, Base

from src.routes.authRoutes import router as auth_router
from src.routes.carRoutes import router as car_router
from src.routes.simulationRoutes import router as simulation_router
from src.routes.analyticsRoutes import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vehicle Health Monitoring API")

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(car_router)
app.include_router(simulation_router)
app.include_router(analytics_router)
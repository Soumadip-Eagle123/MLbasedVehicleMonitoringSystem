import random

def generate_sensor_data():
    return {
        "engine_temperature": random.uniform(80, 120),
        "rpm": random.uniform(2000, 4000),
        "battery_voltage": random.uniform(11, 13),
        "tire_pressure": random.uniform(26, 35),
        "vibration": random.choice(["Low", "Medium", "High"])
    }
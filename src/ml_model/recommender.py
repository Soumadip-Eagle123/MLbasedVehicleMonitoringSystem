def generate_recommendations(data):

    rec = []

    if data["engine_temperature_c"] > 105:
        rec.append("Inspect cooling system")

    if data["vibration_mm_per_s"] > 6:
        rec.append("Check engine mounting and balance")

    if data["battery_voltage"] < 12.0:
        rec.append("Check battery health")

    if data["tire_pressure_psi"] < 30:
        rec.append("Inflate tires to recommended PSI")

    if data["service_history"] == 2:
        rec.append("Immediate full servicing required")

    if not rec:
        rec.append("Vehicle condition is stable")

    return rec
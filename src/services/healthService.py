def calculate_health(temp, rpm, battery, tire, vibration, ml_prediction):
    health = 100

    if temp > 110:
        health -= 20
    if rpm > 3500:
        health -= 10
    if battery < 11.5:
        health -= 15
    if tire < 28:
        health -= 8
    if vibration == "High":
        health -= 12
    if ml_prediction == "High Risk":
        health -= 20

    return max(0, health)
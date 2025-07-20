# Predefined sensor data for 10 intervals
test_data = [
    {"temp_c": 28, "humidity": 45, "light": 250, "soil_moisture": 32, "co2": 1100},
    {"temp_c": 37, "humidity": 30, "light": 850, "soil_moisture": 40, "co2": 1300},
    {"temp_c": 29, "humidity": 42, "light": 950, "soil_moisture": 72, "co2": 900},
    {"temp_c": 38, "humidity": 22, "light": 1200, "soil_moisture": 28, "co2": 1250},
    {"temp_c": 34, "humidity": 50, "light": 450, "soil_moisture": 60, "co2": 1000},
    {"temp_c": 37, "humidity": 20, "light": 1150, "soil_moisture": 29, "co2": 1300},
    {"temp_c": 25, "humidity": 60, "light": 290, "soil_moisture": 33, "co2": 800},
    {"temp_c": 36.5, "humidity": 24, "light": 1120, "soil_moisture": 31, "co2": 1230},
    {"temp_c": 27, "humidity": 38, "light": 300, "soil_moisture": 35, "co2": 1100},
    {"temp_c": 31, "humidity": 39, "light": 1001, "soil_moisture": 34, "co2": 1180}
]

# Simulation function for environmental input
def simulate_input():
    if test_data:
        return test_data.pop(0)
    else:
        print("The list is empty")
        return None  # safely handles end of list

# Watering Control using if-else 
def watering_control(soil_moisture, humidity, temp_c):
    if soil_moisture < 35 and (humidity < 40 or temp_c > 30):
        return "Initiate watering (Full)"
    elif 35 <= soil_moisture <= 50 and temp_c > 35:
        return "Initiate light watering"
    elif soil_moisture > 70:
        return "Skip watering (Too wet)"
    else:
        return "No watering needed"

# Shading Control using match-case 
def shading_control(light_intensity):
    match light_intensity:
        case light_intensity if light_intensity < 300:
            return "Open shades (Very Low Light)"
        case light_intensity if 300 <= light_intensity < 800:
            return "No action (Moderate Light)"
        case light_intensity if 800 <= light_intensity <= 1000:
            return "Close shades partially (High Light)"
        case light_intensity if light_intensity > 1000:
            return "Close shades fully (Very High Light)"

# AI-Driven Risk Alerts 
def risk_alerts(data):
    risk = 0
    if data["temp_c"] > 36:
        risk += 1
    if data["humidity"] < 25:
        risk += 1
    if data["co2"] > 1200:
        risk += 1
    if data["soil_moisture"] < 30:
        risk += 1
    if data["light"] > 1100:
        risk += 1

    if risk >= 3:
        return True, "ALERT: High risk of plant damage!"
    else:
        return False, "Risk level acceptable"

# Moving average of soil moisture to simulate AI trend prediction
def moving_average_trend(soil_moisture_history, trend_range=3):
    if len(soil_moisture_history) < trend_range:
        return "Not enough data for analysis"
    
    avg = sum(soil_moisture_history[-trend_range:]) / trend_range
    if avg < 40:
        return "Recommendation: Increase watering frequency tomorrow."
    elif avg > 70:
        return "Recommendation: Reduce watering frequency tomorrow."
    else:
        return "Recommendation: Watering strategy is balanced."

# Main Simulation Loop 
if __name__ == "__main__":
    soil_moisture_history = []
    consecutive_alerts = 0

    for interval in range(1, 11):  
        print(f"\nInterval {interval}")
        data = simulate_input()
        if data is None:
            break

        # Output clarity and explanation of decisions
        print(f"Temperature: {data['temp_c']:.1f}°C")
        print(f"Humidity: {data['humidity']:.1f}%")
        print(f"Light: {data['light']:.1f} lux")
        print(f"Soil Moisture: {data['soil_moisture']:.1f}%")
        print(f"CO₂ Level: {data['co2']:.1f} ppm")

        print(watering_control(data["soil_moisture"], data["humidity"], data["temp_c"]))
        print(shading_control(data["light"]))

        alert_triggered, alert_message = risk_alerts(data)
        print(alert_message)

        # Track consecutive alerts for escalation
        if alert_triggered:
            consecutive_alerts += 1
        else:
            consecutive_alerts = 0

        if consecutive_alerts >= 2:
            print("CRITICAL RISK FLAG: Immediate action required!")

        # Track soil moisture 
        soil_moisture_history.append(data["soil_moisture"])
        print(moving_average_trend(soil_moisture_history))






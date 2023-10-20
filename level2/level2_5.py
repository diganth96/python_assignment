def analyze_temperature(temperature_readings):
    if not temperature_readings:
        return None

    average_temperature = sum(temperature_readings) / len(temperature_readings)
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)
    return {
        "Average Temperature": average_temperature,
        "Highest Temperature": highest_temperature,
        "Lowest Temperature": lowest_temperature
    }
temperature_readings = [25, 28, 21, 24, 27]
result = analyze_temperature(temperature_readings)
if result:
    print("Average Temperature:", result["Average Temperature"])
    print("Highest Temperature:", result["Highest Temperature"])
    print("Lowest Temperature:", result["Lowest Temperature"])

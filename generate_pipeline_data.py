import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

# Set up parameters for the dataset
num_months = 12
time_interval_minutes = 30  # Recording interval (every 30 minutes)
total_hours = num_months * 30 * 24  # Total hours in 12 months (approx)
num_records = total_hours * (60 // time_interval_minutes)  # Total data points

# Initialize data lists
timestamps = []
pressure_data = []
flow_rate_data = []
temperature_data = []
wear_factor_data = []
valve_status_data = []
pump_speed_data = []
vibration_level_data = []
corrosion_level_data = []
leak_detection_data = []
oil_quality_data = []
pressure_loss_data = []
pump_efficiency_data = []
humidity_data = []
ambient_temp_data = []
distance_from_source_data = []
maintenance_status_data = []
pressure_regulator_data = []
flow_control_valve_data = []
oil_density_data = []
oil_viscosity_data = []
pipeline_altitude_data = []
pipeline_diameter_data = []
sand_content_data = []
pipeline_coating_data = []
oil_sulfur_content_data = []
scheduled_maintenance_data = []
anomalies = []

# Function to simulate weather conditions (affecting pipeline pressure and temperature)
def simulate_weather():
    weather = random.choice(["clear", "storm", "hot", "cold"])
    if weather == "storm":
        pressure_variation = random.uniform(10, 30)  # Storms can increase pressure
        temperature_variation = random.uniform(5, 15)  # Slight rise in temp
    elif weather == "hot":
        pressure_variation = random.uniform(-5, 5)
        temperature_variation = random.uniform(10, 25)  # Higher temperature
    elif weather == "cold":
        pressure_variation = random.uniform(-10, 5)
        temperature_variation = random.uniform(-20, -5)  # Colder temperature
    else:
        pressure_variation = random.uniform(-5, 5)  # Stable conditions
        temperature_variation = random.uniform(-2, 2)
    return pressure_variation, temperature_variation

# Function to simulate anomalies (pressure spikes, flow rate drops, temperature surges)
def simulate_anomalies(wear_factor):
    if wear_factor > 50 and random.random() < 0.1:  # Higher wear increases chances of anomaly
        return True, random.uniform(50, 100), random.uniform(-50, -200), random.uniform(5, 20)  # Anomalous pressure, flow, temp
    return False, 0, 0, 0

# Generate synthetic data for 12 months
current_time = datetime.now() - timedelta(days=num_months * 30)
wear_factor = 0  # Initial wear factor
last_maintenance = current_time - timedelta(days=random.randint(30, 90))  # Random last maintenance
for i in range(num_records):
    timestamps.append(current_time)

    # Baseline sensor readings (fluctuate within a certain range)
    pressure = np.random.normal(800, 30)  # Pressure in PSI (around 800, with some variance)
    flow_rate = np.random.normal(400, 50)  # Flow rate in barrels per hour (around 400)
    temperature = np.random.normal(100, 10)  # Temperature in Fahrenheit (around 100)
    
    # Simulate wear factor over time (increases slowly)
    wear_factor += 0.01
    if wear_factor > 100:
        wear_factor = 100  # Cap wear factor at 100%

    # Apply weather conditions
    pressure_variation, temp_variation = simulate_weather()
    pressure += pressure_variation
    temperature += temp_variation

    # Simulate additional features
    valve_status = random.choice(["open", "closed"])
    pump_speed = np.random.normal(1800, 100)  # Pump speed in RPM
    vibration_level = np.random.normal(3, 0.5)  # Vibration level in mm/s
    corrosion_level = wear_factor * 0.5  # Corrosion increases with wear factor
    leak_detection = 1 if random.random() < 0.05 else 0  # Random leaks
    oil_quality = random.choice(["Light", "Medium", "Heavy"])
    pressure_loss = np.random.normal(5, 2)  # Pressure loss across the pipeline
    pump_efficiency = np.random.normal(90, 5)  # Pump efficiency as a percentage
    humidity = np.random.normal(50, 10)  # Humidity percentage
    ambient_temp = np.random.normal(70, 10)  # Ambient temperature in Fahrenheit
    distance_from_source = np.random.normal(50, 10)  # Distance from source in km
    maintenance_status = last_maintenance
    pressure_regulator_status = random.choice(["active", "inactive"])
    flow_control_valve = np.random.normal(80, 10)  # Valve openness in percentage
    oil_density = np.random.normal(0.9, 0.05)  # Oil density in g/cm³
    oil_viscosity = np.random.normal(20, 5)  # Oil viscosity in centipoise
    pipeline_altitude = np.random.normal(500, 50)  # Altitude in meters
    pipeline_diameter = np.random.normal(1.0, 0.1)  # Diameter in meters
    sand_content = np.random.normal(5, 1)  # Sand content in ppm
    pipeline_coating = max(100 - wear_factor, 0)  # Coating degrades with wear factor
    oil_sulfur_content = np.random.normal(2.0, 0.5)  # Sulfur content percentage
    scheduled_maintenance = 1 if random.random() < 0.1 else 0  # Random scheduled maintenance
    
    # Apply anomalies (if wear factor is high or randomly triggered)
    anomaly, pressure_spike, flow_drop, temp_surge = simulate_anomalies(wear_factor)
    if anomaly:
        pressure += pressure_spike
        flow_rate += flow_drop
        temperature += temp_surge
        anomalies.append(1)  # Mark as an anomaly
    else:
        anomalies.append(0)

    # Append readings to data lists
    pressure_data.append(round(pressure, 2))
    flow_rate_data.append(round(flow_rate, 2))
    temperature_data.append(round(temperature, 2))
    wear_factor_data.append(round(wear_factor, 2))
    valve_status_data.append(valve_status)
    pump_speed_data.append(round(pump_speed, 2))
    vibration_level_data.append(round(vibration_level, 2))
    corrosion_level_data.append(round(corrosion_level, 2))
    leak_detection_data.append(leak_detection)
    oil_quality_data.append(oil_quality)
    pressure_loss_data.append(round(pressure_loss, 2))
    pump_efficiency_data.append(round(pump_efficiency, 2))
    humidity_data.append(round(humidity, 2))
    ambient_temp_data.append(round(ambient_temp, 2))
    distance_from_source_data.append(round(distance_from_source, 2))
    maintenance_status_data.append(maintenance_status.strftime("%Y-%m-%d %H:%M:%S"))
    pressure_regulator_data.append(pressure_regulator_status)
    flow_control_valve_data.append(round(flow_control_valve, 2))
    oil_density_data.append(round(oil_density, 3))
    oil_viscosity_data.append(round(oil_viscosity, 2))
    pipeline_altitude_data.append(round(pipeline_altitude, 2))
    pipeline_diameter_data.append(round(pipeline_diameter, 2))
    sand_content_data.append(round(sand_content, 2))
    pipeline_coating_data.append(round(pipeline_coating, 2))
    oil_sulfur_content_data.append(round(oil_sulfur_content, 2))
    scheduled_maintenance_data.append(scheduled_maintenance)

    # Increment time by the interval
    current_time += timedelta(minutes=time_interval_minutes)

# Create DataFrame
data = {
    "Timestamp": timestamps,
    "Pressure (PSI)": pressure_data,
    "Flow Rate (bbl/h)": flow_rate_data,
    "Temperature (F)": temperature_data,
    "Wear Factor (%)": wear_factor_data,
    "Valve Status": valve_status_data,
    "Pump Speed (RPM)": pump_speed_data,
    "Vibration Level (mm/s)": vibration_level_data,
    "Corrosion Level (%)": corrosion_level_data,
    "Leak Detected": leak_detection_data,
    "Oil Quality": oil_quality_data,
    "Pressure Loss (PSI)": pressure_loss_data,
    "Pump Efficiency (%)": pump_efficiency_data,
    "Humidity (%)": humidity_data,
    "Ambient Temperature (F)": ambient_temp_data,
    "Distance from Source (km)": distance_from_source_data,
    "Last Maintenance": maintenance_status_data,
    "Pressure Regulator Status": pressure_regulator_data,
    "Flow Control Valve (%)": flow_control_valve_data,
    "Oil Density (g/cm³)": oil_density_data,
    "Oil Viscosity (cP)": oil_viscosity_data,
    "Pipeline Altitude (m)": pipeline_altitude_data,
    "Pipeline Diameter (m)": pipeline_diameter_data,
    "Sand Content (ppm)": sand_content_data,
    "Pipeline Coating Condition (%)": pipeline_coating_data,
    "Oil Sulfur Content (%)": oil_sulfur_content_data,
    "Scheduled Maintenance": scheduled_maintenance_data,
    "Anomaly": anomalies
}
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("pipeline_sensor_data_enhanced.csv", index=False)

print("Enhanced dataset generated and saved as 'pipeline_sensor_data_enhanced.csv'")

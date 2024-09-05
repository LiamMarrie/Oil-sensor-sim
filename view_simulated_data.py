import numpy as np
import pandas as pd
import random
import time

# Set a random seed based on the current time (or some other varying factor)
np.random.seed(int(time.time()))  # This will ensure different results every time
random.seed(int(time.time()))  # For other random operations

# Simulate new sensor data with different values
simulated_data = np.random.normal(loc=100, scale=10, size=(100, 23))  # Example random data

# Convert it into a Pandas DataFrame for easier viewing
simulated_df = pd.DataFrame(simulated_data, columns=[
    'Pressure (PSI)', 'Flow Rate (bbl/h)', 'Temperature (F)', 
    'Wear Factor (%)', 'Vibration Level (mm/s)', 'Corrosion Level (%)',
    'Leak Detected', 'Pressure Loss (PSI)', 'Pump Efficiency (%)', 
    'Humidity (%)', 'Ambient Temperature (F)', 'Distance from Source (km)', 
    'Flow Control Valve (%)', 'Oil Density (g/cm³)', 'Oil Viscosity (cP)', 
    'Pipeline Altitude (m)', 'Pipeline Diameter (m)', 'Sand Content (ppm)', 
    'Pipeline Coating Condition (%)', 'Oil Sulfur Content (%)',
    'Scheduled Maintenance', 'Anomaly', 'Additional Feature'
])

# Display the first few rows of the simulated data
print(simulated_df.head())

# Save the DataFrame to an Excel file
simulated_df.to_excel('simulated_sensor_data.xlsx', index=False)

print("Data has been saved to 'simulated_sensor_data.xlsx'.")

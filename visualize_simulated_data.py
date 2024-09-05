import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the simulated data
simulated_data = np.load('simulated_sensor_data.npy')

# Corrected column names to match the shape (23 columns)
columns = [
    'Pressure (PSI)', 'Flow Rate (bbl/h)', 'Temperature (F)', 
    'Wear Factor (%)', 'Vibration Level (mm/s)', 'Corrosion Level (%)',
    'Leak Detected', 'Pressure Loss (PSI)', 'Pump Efficiency (%)', 
    'Humidity (%)', 'Ambient Temperature (F)', 'Distance from Source (km)', 
    'Flow Control Valve (%)', 'Oil Density (g/cm³)', 'Oil Viscosity (cP)', 
    'Pipeline Altitude (m)', 'Pipeline Diameter (m)', 'Sand Content (ppm)', 
    'Pipeline Coating Condition (%)', 'Oil Sulfur Content (%)',
    'Scheduled Maintenance', 'Anomaly', 'New Feature (if applicable)'
]

# Convert it into a Pandas DataFrame for easier viewing
simulated_df = pd.DataFrame(simulated_data, columns=columns)

# Plot the first 100 steps of simulated pressure, temperature, and flow rate
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(simulated_df['Pressure (PSI)'][:100])
plt.title('Simulated Pressure (PSI)')

plt.subplot(3, 1, 2)
plt.plot(simulated_df['Flow Rate (bbl/h)'][:100])
plt.title('Simulated Flow Rate (bbl/h)')

plt.subplot(3, 1, 3)
plt.plot(simulated_df['Temperature (F)'][:100])
plt.title('Simulated Temperature (F)')

plt.tight_layout()
plt.show()

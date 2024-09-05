import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("pipeline_sensor_data_enhanced.csv")

# Drop any columns that are not needed for the AI model
df = df.drop(columns=['Timestamp', 'Oil Quality', 'Last Maintenance', 'Valve Status', 'Pressure Regulator Status'])

# Check for missing values (fill if necessary)
df.fillna(method='ffill', inplace=True)

# Normalize the dataset using StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Save the scaler for later use (when we need to reverse the scaling)
np.save('scaler.npy', scaler)

# Function to create sequences from the data for time-series modeling
def create_sequences(data, seq_length):
    sequences = []
    targets = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i+seq_length])
        targets.append(data[i+seq_length])  # Predict the next step
    return np.array(sequences), np.array(targets)

# Define sequence length (e.g., 10 previous steps to predict the next one)
sequence_length = 10

# Create sequences
X, y = create_sequences(scaled_data, sequence_length)

# Save the processed sequences
np.save('X.npy', X)
np.save('y.npy', y)

print("Data preprocessing complete. Sequences saved.")

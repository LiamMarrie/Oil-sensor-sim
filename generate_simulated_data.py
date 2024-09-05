import numpy as np
import tensorflow as tf

# Load the trained model and the scaler
model = tf.keras.models.load_model('trained_lstm_model.h5')
scaler = np.load('scaler.npy', allow_pickle=True).item()

# Load test data to get an initial seed sequence
X_test = np.load('X.npy')[800:]  # For example, use part of the test data

# Function to simulate sensor data
def simulate_sensor_data(model, initial_sequence, num_steps):
    simulated_data = []
    current_sequence = initial_sequence

    for _ in range(num_steps):
        prediction = model.predict(current_sequence[np.newaxis, :, :])[0]
        simulated_data.append(prediction)

        # Shift the current sequence and append the predicted value
        current_sequence = np.vstack([current_sequence[1:], prediction])

    return np.array(simulated_data)

# Select an initial sequence from the test data
initial_sequence = X_test[0]

# Generate 100 time steps of simulated data
simulated_data = simulate_sensor_data(model, initial_sequence, 100)

# Inverse transform the scaled data to original values
simulated_data = scaler.inverse_transform(simulated_data)

# Save the simulated data
np.save('simulated_sensor_data.npy', simulated_data)

print("Simulated sensor data generated and saved.")

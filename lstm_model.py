import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np

# Load the preprocessed data
X = np.load('X.npy')
y = np.load('y.npy')

# Define the LSTM model architecture
model = Sequential()

# First LSTM layer with dropout to avoid overfitting
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))

# Second LSTM layer
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))

# Dense layer to produce the output
model.add(Dense(X.shape[2]))  # Output dimension matches the number of features

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Print the model summary
model.summary()

# Save the model architecture
model.save('lstm_model.h5')

print("LSTM model created and saved.")

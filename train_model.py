import numpy as np
import tensorflow as tf

# Load the LSTM model and the data
X = np.load('X.npy')
y = np.load('y.npy')
model = tf.keras.models.load_model('lstm_model.h5')

# Recompile the model after loading it
model.compile(optimizer='adam', loss='mean_squared_error')

# Split data into training and testing sets
split = int(0.8 * len(X))  # 80% training, 20% testing
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=64, validation_data=(X_test, y_test))

# Save the trained model
model.save('trained_lstm_model.h5')

# Save the training history
np.save('history.npy', history.history)

print("Model training complete. Trained model saved.")

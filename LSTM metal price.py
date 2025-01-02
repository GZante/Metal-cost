import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_percentage_error
from keras.models import Sequential
from keras.layers import LSTM, Dense, Bidirectional
from keras.optimizers import Adam
import yfinance as yf

# List of metals and their corresponding ticker symbols
metals = {
    'Gold': 'GC=F',
    'Silver': 'SI=F',
    'Platinum': 'PL=F',
    'Palladium': 'PA=F',
    'Aluminum': 'ALI=F',
    'Copper': 'HG=F'
}

def create_sequences(data, seq_length):
    """
    Create sequences of data for LSTM input.

    Parameters:
    data (np.array): The input data.
    seq_length (int): The length of the sequences.

    Returns:
    np.array: The sequences and their corresponding targets.
    """
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:i + seq_length]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

def process_metal(metal_name, ticker):
    """
    Process and forecast for a given metal.

    Parameters:
    metal_name (str): The name of the metal.
    ticker (str): The ticker symbol of the metal.
    """
    print(f"Processing {metal_name}...")

    # Step 1: Download historical price data
    data = yf.download(ticker, start='2000-01-01', end='2024-12-31')

    # Step 2: Use the 'Close' price for forecasting
    data = data[['Close']]

    # Step 3: Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Step 4: Create sequences
    seq_length = 60  # Use 60 days of historical data to forecast the next day's price
    X, y = create_sequences(scaled_data, seq_length)

    # Reshape data for LSTM input
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Step 5: Split into training and test sets
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Step 6: Build the Bidirectional LSTM model
    model = Sequential()
    model.add(Bidirectional(LSTM(64, return_sequences=False, input_shape=(seq_length, 1))))
    model.add(Dense(1))

    # Set the learning rate
    optimizer = Adam(learning_rate=0.01)
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Step 7: Train the model
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=2)

    # Step 8: Make forecasts
    train_forecast = model.predict(X_train)
    test_forecast = model.predict(X_test)

    # Step 9: Inverse transform the forecasts
    train_forecast = scaler.inverse_transform(train_forecast)
    y_train = scaler.inverse_transform(y_train.reshape(-1, 1))
    test_forecast = scaler.inverse_transform(test_forecast)
    y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

    # Step 10: Calculate metrics
    mape_train = mean_absolute_percentage_error(y_train, train_forecast)
    accuracy_train = 1 - mape_train

    mape_test = mean_absolute_percentage_error(y_test, test_forecast)
    accuracy_test = 1 - mape_test

    # Print the error metrics
    print(f'{metal_name} Train MAPE: {mape_train}, Train Accuracy: {accuracy_train}')
    print(f'{metal_name} Test MAPE: {mape_test}, Test Accuracy: {accuracy_test}')

    # Step 11: Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, scaler.inverse_transform(scaled_data), label='Original Data')
    plt.plot(data.index[seq_length:seq_length + len(train_forecast)], train_forecast, label='Train Forecast')
    plt.plot(data.index[seq_length + len(train_forecast):seq_length + len(train_forecast) + len(test_forecast)], test_forecast, label='Test Forecast')
    plt.title(f'{metal_name} Price Forecast')
    plt.legend()
    plt.show()

# Process each metal
for metal_name, ticker in metals.items():
    process_metal(metal_name, ticker)

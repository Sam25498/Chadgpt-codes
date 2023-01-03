import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("EURUSD_4h.csv")

# Convert the date strings to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Set the datetime column as the index
df.set_index('Date', inplace=True)

# Calculate the momentum
df['Momentum'] = df['Close'].diff(periods=12)

# Buy when the momentum is positive
df['Position'] = np.where(df['Momentum'] > 0, 1, 0)


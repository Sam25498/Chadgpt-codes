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

# Sell when the momentum is negative
df['Position'] = np.where(df['Momentum'] < 0, -1, df['Position'])

# Calculate the daily returns
df['Returns'] = df['Close'].pct_change(periods=1)

# Calculate the strategy returns
df['Strategy'] = df['Returns'] * df['Position']







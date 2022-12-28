# First, we need to import the necessary libraries
import tradingview as tv
import pandas as pd

# Next, we need to retrieve the data for the EURUSD 1 hour chart
data = tv.fetch_ohlcv("EURUSD", "1h")

# Now, we can convert the data into a pandas DataFrame for easier analysis
df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])

# We can then use the 'high' and 'low' columns to detect double tops and double bottoms
# For double tops, we will look for two consecutive highs that are relatively close to each other
# For double bottoms, we will look for two consecutive lows that are relatively close to each other

# To do this, we can define a threshold distance (in pips) that we will use to determine if two highs or lows are "close"
threshold_distance = 20

# Now, we can loop through the data and check for double tops and double bottoms
for i in range(1, len(df) - 1):
    # Check for double tops
    if (df.iloc[i]["high"] - df.iloc[i-1]["high"] < threshold_distance) and (df.iloc[i+1]["high"] - df.iloc[i]["high"] < threshold_distance):
        print("Double top detected at", df.iloc[i]["timestamp"])

    # Check for double bottoms
    if (df.iloc[i-1]["low"] - df.iloc[i]["low"] < threshold_distance) and (df.iloc[i]["low"] - df.iloc[i+1]["low"] < threshold_distance):
        print("Double bottom detected at", df.iloc[i]["timestamp"])


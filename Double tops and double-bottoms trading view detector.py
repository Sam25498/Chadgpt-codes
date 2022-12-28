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


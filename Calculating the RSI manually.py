#Prompt: write a python function that takes series of data as an argument and using that data create a 14 period rsi indicator values, and return a list of those indicator values from most recent to earlier
"""The Relative Strength Index (RSI) is a popular technical indicator that is used to measure the strength of a security's price action. It compares the magnitude of recent gains to recent losses to determine overbought and oversold conditions of an asset. The RSI is typically calculated using a 14-period time frame, but can be adjusted to suit different trading styles.

Here is a Python function that takes a series of data as an argument and calculates the 14-period RSI:"""

def calculate_rsi(data):
    # Initialize variables
    gain = 0
    loss = 0
    rsi_list = []
    # Iterate through the data to calculate the gain and loss
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            gain += data[i] - data[i-1]
        else:
            loss += data[i-1] - data[i]
    # Calculate the relative strength
    avg_gain = gain / 14
    avg_loss = loss / 14
    rs = avg_gain / avg_loss
    # Calculate the RSI
    rsi = 100 - (100 / (1 + rs))
    rsi_list.append(rsi)
    for i in range(14, len(data)):
        if data[i] > data[i-1]:
            avg_gain = ((avg_gain * 13) + (data[i] - data[i-1])) / 14
            avg_loss = ((avg_loss * 13) + 0) / 14
        else:
            avg_gain = ((avg_gain * 13) + 0) / 14
            avg_loss = ((avg_loss * 13) + (data[i-1] - data[i])) / 14
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        rsi_list.append(rsi)
    return rsi_list[::-1]
"""
This function first initializes gain, loss, and rsi_list variables. Then it iterates through the data and calculates the gain and loss 
using the difference between the current and previous data point. Next, it calculates the relative strength using the average gain and average loss. 
It then uses the relative strength value to calculate the RSI. Finally, it returns the list of RSI values, but in reverse order (from most recent to earlier).

It's important to note that this function assumes that the data is a list or array of numerical values. If the data is in a different format, the function will
need to be modified accordingly. Also, the RSI values are typically considered overbought when above 70 and oversold when below 30.
"""

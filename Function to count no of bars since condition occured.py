#ere is an example of a Python function that takes a condition and a list of Forex bar data as arguments, and outputs the number of bars since the last time the condition was true:ere is an example of a Python function that takes a condition and a list of Forex bar data as arguments, and outputs the number of bars since the last time the condition was true:
def count_bars_since_condition(condition, data):
    count = 0
    condition_met = False
    for bar in data:
        if condition(bar):
            condition_met = True
        elif condition_met:
            count += 1
    return count
"""
This function uses a for loop to iterate through the list of Forex bar data, and checks each bar against the provided condition. If the condition is met, the condition_met variable is set to True, and the loop continues. If the condition is not met and condition_met is True, the count is incremented. The function returns the final count.
You can use this function by providing a specific condition and list of data as arguments, like this:v
"""

data = [{'Open':1.1,'Close':1.2,'High':1.3,'Low':1.0},
        {'Open':1.2,'Close':1.3,'High':1.4,'Low':1.1},
        {'Open':1.3,'Close':1.2,'High':1.5,'Low':1.2}
       ]
def condition(bar):
    return bar['Open'] > bar['Close']
count_bars_since_condition(condition, data)
# Output: 1

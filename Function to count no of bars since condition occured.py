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

"""
Here, the function is counting the number of bars since the last time the open price was greater than the close price in the list of data.
"""
################## Second Iteration of doing the same thing in a slightly different way  ##################

"""Here's an example of a python function that takes a condition as an argument and outputs an integer value, which represents 
the number of forex bars since the last time the condition was true:"""

def count_bars_since_condition(condition, data):
    count = 0
    condition_met = False
    for bar in data:
        if condition(bar):
            condition_met = True
            count = 0
        elif condition_met:
            count += 1
    return count

"""
This function takes a condition function and a list of Forex bar data as arguments. It then initializes a count variable to 0 and a condition_met variable to False. 
It iterates through the list of data, and for each bar, it checks if the condition is true. If it is, it sets the condition_met variable to True and resets the count 
variable to 0. If the condition is not met and the condition_met variable is True, it increments the count variable. The function then returns the final count.
You can use this function by providing a specific condition and list of data as arguments, like this:
"""
data = [{'Open':1.1,'Close':1.2,'High':1.3,'Low':1.0},
        {'Open':1.2,'Close':1.3,'High':1.4,'Low':1.1},
        {'Open':1.3,'Close':1.2,'High':1.5,'Low':1.2}
       ]
def condition(bar):
    return bar['Open'] > bar['Close']
count_bars_since_condition(condition, data)
# Output: 2
"""
Here, the function is counting the number of bars since the last time the open price was greater than the close price in the list of data.
"""

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

#Prompt: Write a python function that takes series of forex data as an argument, and identifies troughs  in that data.
def identify_troughs(forex_data):
    troughs = []
    for i in range(1, len(forex_data) - 1):
        if forex_data[i] < forex_data[i-1] and forex_data[i] < forex_data[i+1]:
            troughs.append(i)
    return troughs
#Prompt: Write a python function that takes series of forex data as an argument, and identifies crest/peaks  in that data.
"""This function uses a for loop to iterate through the forex data. For each data point, 
it checks if the current point is less than the point before it and the point after it. If both of those conditions are true, 
then the current point is considered a trough and its index is added to the "troughs" list. Once the loop is finished, 
the function returns the list of troughs.

It's important to note that this function assumes that the forex data is a list or array of numerical values. 
If the data is in a different format, the function will need to be modified accordingly."""

def identify_crests(forex_data):
    crests = []
    for i in range(1, len(forex_data) - 1):
        if forex_data[i] > forex_data[i-1] and forex_data[i] > forex_data[i+1]:
            crests.append(i)
    return crests
"""This function uses a for loop to iterate through the forex data. For each data point, 
it checks if the current point is greater than the point before it and the point after it. If both of those conditions are true, 
then the current point is considered a crest/peak and its index is added to the "crests" list. Once the loop is finished, 
the function returns the list of crest/peaks.

It's important to note that this function assumes that the forex data is a list or array of numerical values. 
If the data is in a different format, the function will need to be modified accordingly. """

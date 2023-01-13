def identify_troughs(forex_data):
    troughs = []
    for i in range(1, len(forex_data) - 1):
        if forex_data[i] < forex_data[i-1] and forex_data[i] < forex_data[i+1]:
            troughs.append(i)
    return troughs

import pandas as pd
from stockstats import StockDataFrame as Sdf

def crossover(filename):
    data = pd.read_csv(filename)
    stock = Sdf.retype(data)
    signal = stock['macds']  # Your signal line
    macd = stock['macd']  # The MACD that need to cross the signal line
    #                                              to give you a Buy/Sell signal
    listLongShort = ["No data"]  # Since you need at least two days in the for loop
    for i in range(1, len(signal)):
        #                          # If the MACD crosses the signal line upward
        if macd[i] > signal[i] and macd[i - 1] <= signal[i - 1]:
            listLongShort.append("BUY")
        #                          # The other way around
        elif macd[i] < signal[i] and macd[i - 1] >= signal[i - 1]:
            listLongShort.append("SELL")
        #                          # Do nothing if not crossed
        else:
            listLongShort.append("HOLD")
    return listLongShort
    # stock['Advice'] = listLongShort

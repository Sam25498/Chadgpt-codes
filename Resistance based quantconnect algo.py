from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from quantconnect.algorithm import QCAlgorithm
from quantconnect.data.market import TradeBar
from quantconnect.data.custom import Forex
from quantconnect.indicators import CandlestickPatterns

class ForexAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set the start date
        self.SetEndDate(2022, 12, 31)  # Set the end date
        self.SetCash(100000)  # Set the initial capital
        self.AddForex("EURUSD", Resolution.Hour)  # Add the EURUSD pair to the algorithm
        self.bullish_engulfing = CandlestickPatterns.BullishEngulfing(self.Symbol)  # Initialize the bullish engulfing indicator



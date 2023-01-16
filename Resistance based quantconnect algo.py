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


        self.resistance_level = None  # Initialize the resistance level variable
        self.previous_bar = None  # Initialize the previous bar variable

    def OnData(self, data):
        if not data.ContainsKey(self.Symbol):
            return

        bar = data[self.Symbol]  # Get the current bar
        self.bullish_engulfing.Update(bar.EndTime, bar)  # Update the bullish engulfing indicator

  
      # Check if the price has broken the resistance level
        if self.resistance_level is not None and bar.Close > self.resistance_level:
            self.resistance_level = None  # Clear the resistance level

import numpy as np
from quantconnect.algorithm import QCAlgorithm
from quantconnect.indicators import ExponentialMovingAverage
from quantconnect.indicators import RollingWindow

class FibonacciTradingAlgorithm(QCAlgorithm):
    def Initialize(self):
        # Set the cash we'd like to use for our backtest
        # This is ignored in live trading
        self.SetCash(100000)

        # Set the security we'd like to use
        self.symbol = "EURUSD"
        self.AddForex(self.symbol, Resolution.Minute)

        # Set the rolling window size for the max/min price close
        self.window_size = 50

        # Set the Fibonacci retracement levels
        self.entry_level = 0.618
        self.exit_level = 1.0

        # Create a rolling window to track the max/min price close
        self.price_close_window = RollingWindow[float](self.window_size)

        # Create a flag to track whether we are currently in a trade
        self.in_trade = False

        # Schedule an event to fire every 5 minutes
        self.Schedule.On(self.DateRules.Every(DayOfWeek.Monday, DayOfWeek.Tuesday, DayOfWeek.Wednesday, DayOfWeek.Thursday, DayOfWeek.Friday), self.TimeRules.Every(TimeSpan.FromMinutes(5)), self.Trade)

    def OnData(self, data):
        # Update the rolling window with the latest close price
        self.price_close_window.Add(data[self.symbol].Close)

    def Trade(self):
        # Check if we are currently in a trade
        if self.in_trade:
            # If we are, check if we should exit the trade
            # using the exit level as a reference
            if self.Securities[self.symbol].Close < self.exit_level:
                self.Liquidate(self.symbol)
                self.in_trade = False
        else:
            # If we are not in a trade, check if we should enter one
            # using the entry level as a reference
            if self.Securities[self.symbol].Close > self.entry_level:
                self.SetHoldings(self.symbol, 1)
                self.in_trade = True

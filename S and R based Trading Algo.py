from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Indicators")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *
from QuantConnect.Indicators import *

class SupportResistanceAlgorithm(QCAlgorithm):

    def Initialize(self):
        # Set the starting cash balance
        self.SetCash(100000)

        # Set the leverage
        self.SetLeverage(20)

        # Set the trading fees
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)
        
                # Define the symbols we want to trade
        self.symbol = self.AddForex("EURUSD", Resolution.Hour).Symbol

        # Define the moving average indicator
        self.ma = self.EMA(self.symbol, 200)

        # Schedule an event to execute at the end of each trading day
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketClose(self.symbol), self.EndOfDay)

    def OnData(self, data):
        # Check if we have enough data to compute the moving average
        if not self.ma.IsReady:
            return
        
            def EndOfDay(self):
        # Check if we have any open positions
        if self.Portfolio[self.symbol].Quantity == 0:
            return

        # Calculate the support and resistance levels
        holdings = self.Portfolio[self.symbol]
        support = self.Securities[self.symbol].Low
        resistance = self.Securities[self.symbol].High

        # Check if the current price is below the support level
        if holdings.Price < support:
            # Close the position
            self.Liquidate(self.symbol)
        # Check if the current price is above the resistance level
        elif holdings.Price > resistance:
            # Close the position
            self.Liquidate(self.symbol)


        # Check if we have any open positions
        if self.Portfolio[self.symbol].Quantity > 0:
            # Check if the price has crossed below the moving average (indicating a potential trend reversal)
            if self.ma.IsRising and data[self.symbol].Close < self.ma.Current.Value:
                # Close the long position
                self.Liquidate(self.symbol)
        else:
            # Check if the price has crossed above the moving average (indicating a potential trend reversal)
            if self.ma.IsFalling and data[self.symbol].Close > self.ma.Current.Value:
                # Enter a long position
                self.SetHoldings(self.symbol, 1)




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



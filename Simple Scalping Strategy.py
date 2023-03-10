from datetime import timedelta

class SimpleScalpingStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2022, 1, 1)
        self.SetCash(100000)
        self.symbol = self.AddForex("EURUSD", Resolution.Hour).Symbol
        self.fast = self.EMA(self.symbol, 14, Resolution.Hour)
        self.slow = self.EMA(self.symbol, 28, Resolution.Hour)

    def OnData(self, data):
        if not data.ContainsKey(self.symbol):
            return
        if data[self.symbol].Time.date() != self.Time.date():
            return

        if not self.fast.IsReady or not self.slow.IsReady:
            return
        if self.fast > self.slow:
            if self.Portfolio[self.symbol].Quantity <= 0:
                self.Order(self.symbol, 1)
        elif self.fast < self.slow:
            if self.Portfolio[self.symbol].Quantity >= 0:
                self.Order(self.symbol, -1)

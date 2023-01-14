from datetime import timedelta

class SimpleScalpingStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2022, 1, 1)
        self.SetCash(100000)

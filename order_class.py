class BuyOrder:
    def __init__(self, price, quantity, stoploss=None, takeprofit=None):
        self.price = price
        self.quantity = quantity
        self.stoploss = stoploss
        self.takeprofit = takeprofit
        self.status = 'open'
    def close(self, close_price):
        self.close_price = close_price
        self.pl = self.quantity * (self.price - self.close_price)
        self.status = 'closed'
    
class SellOrder:
    def __init__(self, price, quantity, stoploss=None, takeprofit=None):
        self.price = price
        self.quantity = quantity
        self.stoploss = stoploss
        self.takeprofit = takeprofit
        self.status = 'open'
    def close(self, close_price):
        self.close_price = close_price
        self.pl = self.quantity * (self.close_price - self.price)
        self.status = 'closed'
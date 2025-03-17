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
    def check(self, current_price):
        if self.stoploss is not None and current_price <= self.stoploss:
            self.close(current_price)
        elif self.takeprofit is not None and current_price >= self.takeprofit:
            self.close(current_price)
    
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
    def check(self, current_price) -> bool:
        if self.stoploss is not None and current_price >= self.stoploss:
            self.close(current_price)
            return True
        elif self.takeprofit is not None and current_price <= self.takeprofit:
            self.close(current_price)
            return True
        return False
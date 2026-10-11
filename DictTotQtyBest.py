class TradeBook:

    def __init__(self):
        self.trades = []

    def add_trade(self, symbol, qty, price):
        trade = {
            "symbol": symbol,
            "qty": qty,
            "price": price
        }

        self.trades.append(trade)

    def total_quantity(self):
        tot_qty = 0
        
        for trade in self.trades:
            qty = trade["qty"]
            tot_qty += qty
            
        return tot_qty
        

    def total_notional(self):
        tot_not = 0
        
        for trade in self.trades:
            qty = trade["qty"]
            price = trade["price"]
            
            notional = qty * price
            tot_not += notional
            
        return tot_not
    
    
book = TradeBook()

book.add_trade("AAPL", 100, 180.0)
book.add_trade("MSFT", 50, 400.0)
book.add_trade("AAPL", 25, 182.0)

print(book.total_quantity())   # expected 175
print(book.total_notional())   # expected 42550.0
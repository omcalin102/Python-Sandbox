class TradeBook:

    def __init__(self):
        self.trades = []

    def add_trade(self, symbol, side, qty, price):

        trade = {
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price
        }

        self.trades.append(trade)

    def trade_count(self):
        # Return the total number of trades currently stored.
        for trade in self.trades:
            return len(self.trades)
        

    def quantity_by_symbol(self):
        # Return a dictionary containing total quantity by symbol.
        # Ignore BUY/SELL direction here.
        #
        # Example:
        # {
        #     "AAPL": 175,
        #     "MSFT": 50
        # }
        symb_qty = {}
        
        for trade in self.trades:
            symbol = trade["symbol"]
            qty = trade["qty"]
            
            symb_qty[symbol] = symb_qty.get(symbol, 0) + qty
        
        return symb_qty

    def net_quantity_by_symbol(self):
        # Return a dictionary containing net quantity by symbol.
        #
        # BUY quantities are positive.
        # SELL quantities are negative.
        #
        # Example:
        # {
        #     "AAPL": 25,
        #     "MSFT": -50
        # }
        
        symb_net = {}
        
        for trade in self.trades:
            symbol = trade["symbol"]
            qty = trade["qty"]
            side = trade["side"]
            
            if side == "BUY":
                symb_net[symbol] = symb_net.get(symbol, 0) + qty
            elif side == "SELL":
                symb_net[symbol] = symb_net.get(symbol, 0) - qty
            
        return symb_net
            
    
    
def run_test(name, actual, expected):
    if actual == expected:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")


book = TradeBook()

book.add_trade("AAPL", "BUY", 100, 180.0)
book.add_trade("MSFT", "SELL", 50, 400.0)
book.add_trade("AAPL", "SELL", 75, 182.0)


run_test(
    "trade_count",
    book.trade_count(),
    3
)

run_test(
    "quantity_by_symbol",
    book.quantity_by_symbol(),
    {
        "AAPL": 175,
        "MSFT": 50
    }
)

run_test(
    "net_quantity_by_symbol",
    book.net_quantity_by_symbol(),
    {
        "AAPL": 25,
        "MSFT": -50
    }
)
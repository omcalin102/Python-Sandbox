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
        return len(self.trades) 
        
        pass

    def total_quantity(self):
        tot_qty = 0
        for trade in self.trades:
            tot_qty += trade["qty"]
            
        return total
            
        pass

    def total_notional(self):
        tot_not = 0
        
        for trade in self.trades:
            qty = trade["qty"]
            price = trade["price"]
 
            notional = qty * price
            tot_not += notional
        return(symb, tot_not)
        pass

    def quantity_by_symbol(self):
        qty_symb = {}
        
        for trade in self.trade:
            qty = trade["qty"]
            symbol = trade["symbol"]
            
            for symbol in trades:
                qty_symb[symbol] = get.qty_symb(symbol, 0) + qty
                
        print(symbol, qty_symb)
        pass
    
    
def test_trade_count():
    book = TradeBook()

    book.add_trade("AAPL", "BUY", 100, 180.0)
    book.add_trade("MSFT", "SELL", 50, 400.0)

    assert book.trade_count() == 2


def test_total_quantity():
    book = TradeBook()

    book.add_trade("AAPL", "BUY", 100, 180.0)
    book.add_trade("MSFT", "SELL", 50, 400.0)

    assert book.total_quantity() == 150


def test_total_notional():
    book = TradeBook()

    book.add_trade("AAPL", "BUY", 100, 180.0)
    book.add_trade("MSFT", "SELL", 50, 400.0)

    assert book.total_notional() == 38000.0


def test_quantity_by_symbol():
    book = TradeBook()

    book.add_trade("AAPL", "BUY", 100, 180.0)
    book.add_trade("MSFT", "SELL", 50, 400.0)
    book.add_trade("AAPL", "BUY", 75, 181.0)

    assert book.quantity_by_symbol() == {
        "AAPL": 175,
        "MSFT": 50
    }
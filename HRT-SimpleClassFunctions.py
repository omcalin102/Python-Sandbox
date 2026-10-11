class PositionBook:

    def __init__(self):
        self.positions = []

    def add_position(self, symbol, qty, price):
        position = {
            "symbol": symbol,
            "qty": qty,
            "price": price
        }

        self.positions.append(position)

    def position_count(self):
        return len(self.positions)
        pass

    def total_quantity(self):
        tot_qty = 0
        
        for position in self.positions:
            qty = position["qty"]
            
            tot_qty += qty
        return(tot_qty)
        pass

    def total_value(self):
        tot_not = 0
        
        for position in self.positions:
            qty = position["qty"]
            price = position["price"]
            
            notional = qty * price
            
            tot_not += notional
        return(tot_not)
        pass

    def quantity_by_symbol(self):
        qty_symb = {}
        
        for position in self.positions:
            symbol = position["symbol"]
            qty = position["qty"]
            price = position["price"]
            
            qty_symb[symbol] = qty_symb.get(symbol, 0) + qty
            
        return(qty_symb)
        pass


# ---------------- TESTS ----------------

def run_test(name, actual, expected):
    if actual == expected:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")


book = PositionBook()

book.add_position("AAPL", 100, 180.0)
book.add_position("MSFT", 50, 400.0)
book.add_position("AAPL", 25, 182.0)


run_test(
    "position_count",
    book.position_count(),
    3
)

run_test(
    "total_quantity",
    book.total_quantity(),
    175
)

run_test(
    "total_value",
    book.total_value(),
    42550.0
)

run_test(
    "quantity_by_symbol",
    book.quantity_by_symbol(),
    {
        "AAPL": 125,
        "MSFT": 50
    }
)
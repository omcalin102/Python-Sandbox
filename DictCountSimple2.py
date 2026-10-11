trades = [
    ("AAPL", 100),
    ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 40),
    ("MSFT", 25)
]

symb_qty = {}

for symb, qty in trades:
    symb_qty[symb] = symb_qty.get(symb, 0) + qty
    
print(symb_qty)
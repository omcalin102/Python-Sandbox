trades = [
    ("AAPL", "BUY", 100),
    ("MSFT", "SELL", 50),
    ("AAPL", "SELL", 40),
    ("TSLA", "BUY", 75),
    ("MSFT", "BUY", 20)
]

symb_qty = {}

for symb, side, qty in trades:
    if side == "BUY":
        symb_qty[symb] = symb_qty.get(symb, 0) + qty
    if side == "SELL":
        symb_qty[symb] = symb_qty.get(symb, 0) - qty
        
print(symb_qty)
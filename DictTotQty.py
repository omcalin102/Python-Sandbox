trades = [ ("AAPL", 100),     ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 40),
    ("MSFT", 25)
]

totalqty = {}

for symb, qty in trades:
    totalqty[symb] = totalqty.get(symb, 0) + qty
    
print(totalqty)
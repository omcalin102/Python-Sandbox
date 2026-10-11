trades = [
    ("AAPL", 100),
    ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 200),
    ("MSFT", 25)
]

def largest_total(trades):
    symb_qty = {}
    
    for symb, qty in trades:
        symb_qty[symb] = symb_qty.get(symb, 0) + qty
        
    best_symb = None
    best_qty = -1
    
    for symb, qty in symb_qty.items():
        if qty > best_qty:
            best_qty = qty
            best_symb = symb
            
    return(best_symb, best_qty)

print(largest_total(trades = [
    ("AAPL", 100),
    ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 200),
    ("MSFT", 25)
]))
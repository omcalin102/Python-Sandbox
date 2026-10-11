def top_symbol(trades):
    totals = {}
    
    for symb, qty in trades:
        totals[symb] = totals.get(symb, 0) + qty
        
    best_symb = None
    best_tot = 0
    
    for symb, qty in totals.items():
        if qty > best_tot:
            best_tot = qty
            best_symb = symb
            
    return best_symb, best_tot


print(top_symbol(trades = [
    ("AAPL", 100),
    ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 200),
    ("MSFT", 25)
]))


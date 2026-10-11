def largest_position(trades):
    symb_qty = {}
    
    for symb, side, qty in trades:
        if side == "BUY":
            symb_qty[symb] = symb_qty.get(symb, 0) + qty
        if side == "SELL":
            symb_qty[symb] = symb_qty.get(symb, 0) - qty
            
    best_symb = None
    best_qty = -1
    
    for symb, tot_qty in symb_qty.items():
        if tot_qty > best_qty:
            best_qty = tot_qty
            best_symb = symb
            
    return best_symb

print(largest_position(trades = [
    ("AAPL", "BUY", 100),
    ("MSFT", "SELL", 150),
    ("AAPL", "SELL", 40),
    ("TSLA", "BUY", 75),
    ("MSFT", "BUY", 20)
]))
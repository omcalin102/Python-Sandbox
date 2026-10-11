def largest_net_position(trades):
    net = {}
    
    for symbol, side, qty in trades:
        if side == "BUY":
            net[symbol] = net.get(symbol, 0) + qty
        if side == "SELL":
            net[symbol] = net.get(symbol, 0) - qty
            
    best_qty = -1
    best_symb = None
    
    for symbol, qty in net.items():
        if qty > best_qty:
            best_qty = qty
            best_symb = symbol
            
    return(best_symb, best_qty)

print(largest_net_position(trades = [
    ("AAPL", "BUY", 100),
    ("MSFT", "SELL", 50),
    ("AAPL", "SELL", 40),
    ("TSLA", "BUY", 75),
    ("MSFT", "BUY", 20)
]))
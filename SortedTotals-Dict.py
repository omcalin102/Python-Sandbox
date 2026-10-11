def sorted_totals(trades):
    totals = {}
    
    for symb, qty in trades:
        totals[symb] = totals.get(symb, 0) + qty
        
    result = sorted(
        totals.items(),
        key=lambda x: x[1],
        reverse = True
    )
    
    return result


print(sorted_totals(trades = [
    ("AAPL", 100),
    ("MSFT", 50),
    ("AAPL", 75),
    ("TSLA", 200),
    ("MSFT", 25)
]))
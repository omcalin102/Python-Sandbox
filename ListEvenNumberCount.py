symbols = ["AAPL", "MSFT", "AAPL", "TSLA", "MSFT", "AAPL"]

symb_count = {}

for symb in symbols:
    symb_count[symb] = symb_count.get(symb, 0) + 1
    
print(symb_count)
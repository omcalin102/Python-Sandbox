lines = [
    "AAPL,100,180.5",
    "MSFT,50,420.0",
    "TSLA,80,250.0"
]

for line in lines:
    parts = line.split(",")
    
    symbol = parts[0]
    qty = int(parts[1])
    price = float(parts[2])
    
    notional = qty * price
    
    print (symbol, notional)
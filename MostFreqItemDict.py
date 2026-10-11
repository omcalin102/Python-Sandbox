def most_freq(items):
    
    count = {}
    top_item = None
    top_count = 0
    
    for item in items:
        count[item] = count.get(item, 0) + 1
        
    for item, counts in count.items():
        if counts > top_count:
            top_item = item
            top_count = counts
            
    return top_item, top_count

print(most_freq(["AAPL", "AAPL", "PEAR", "NFST", "FSTS", "AAPL"]))
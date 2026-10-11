def first_duplicate(items):
    
    seen = set()
    
    for item in items:
        if item in seen:
            return item
        
        seen.add(item)
        
    return None


print(first_duplicate([3, 4, 6, 2, 4, 3]))
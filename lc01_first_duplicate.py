def first_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        
        seen.add(num)
    
    return None

print(first_duplicate([4, 2, 6, 78, 4, 5]))
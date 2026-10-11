def two_sum(nums, target):
    seen = set()
    
    for num in nums:
        needed = target - num
        
        if needed in seen:
            return needed, num
        
        seen.add(num)
        
    return None

print(two_sum([2, 5, 1, 3], 6))
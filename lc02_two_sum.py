def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        needed = target - num
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i
        
    return None

print(two_sum([2, 5, 1, 5, 7], 9))
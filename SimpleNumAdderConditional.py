def count_targets(nums, target):
    count = 0
    
    for num in nums:
        if num == target:
            count += 1
            
    return count

print(count_targets([3, 5, 2, 56, 5, 7, 3], 5))



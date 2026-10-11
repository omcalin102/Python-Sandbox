def largest_value(nums):
    largest = 0
    
    for num in nums:
        if num > largest:
            largest = num
            
    return largest

print(largest_value([3, 7, 22, 5, 7, 44, 5]))

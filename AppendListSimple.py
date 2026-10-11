def sum_even(nums):
    sum = 0
    
    for num in nums:
        if num % 2 == 0:
            sum += num
            
    return sum

print(sum_even([3, 5, 2, 4, 6, 3, 4]))

nums = [3, 5, 6, 22, 15]

total = 0

for num in nums:
    if num > 10:
        total += num
        
print(total)

def count_targets(nums, target):
    count = 0
    
    for num in nums:
        if num == target:
            count += 1
            
    return count


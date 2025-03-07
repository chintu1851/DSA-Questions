def setMismatch(nums):
    num_set = set()
    duplicate = -1
    n = len(nums)
    for num in nums:
        
        if num in num_set:
            duplicate = num
        num_set.add(num)
    print(num_set)
    # Find missing number
    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break
    
    return [duplicate, missing]

# Test case
nums = [4, 3, 3, 1]
print(setMismatch(nums))  # Output: [3, 2]

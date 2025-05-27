def pattern(nums):
    stack = []
    second = float('-inf')
    
    for i in range(len(nums) - 1, -1, -1):  # Fixed the loop
        if nums[i] < second:
            return True
        while stack and stack[-1] < nums[i]:
            second = stack.pop()
        print(stack)
        stack.append(nums[i])
        print(stack)
    return False  # if no pattern found
nums = [3, 1, 4, 2]
print(pattern(nums))  # Output: True

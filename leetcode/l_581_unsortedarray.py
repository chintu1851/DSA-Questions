def unsortedarray(nums):
    left=len(nums)
    right=0
    stack=[]
    for i in range(len(nums)):
        while stack and nums[stack[-1]]>nums[i]:
            print(stack[-1])
            left=min(left,stack.pop())
        stack.append(i)
    print(stack)
    stack=[]        
    for i in range(len(nums)-1,-1,-1):
        while stack and nums[stack[-1]]<nums[i]:
            right = max(right, stack.pop())
        stack.append(i)
        
    print(stack)
nums = [2, 6, 4, 8, 10, 9, 15]
unsortedarray(nums)

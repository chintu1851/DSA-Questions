def maxelements(nums):
    stack=[]
    n=len(nums)
    result=[-1] * len(nums)
    for i in range(2*n):
        while stack and nums[stack[-1]]<nums[i%n]:
            print("--------------------inside loop--------------------")
            result[stack.pop()] = nums[i%n]
        if i<n:
            stack.append(i)
        print("this is stack",stack)
        print("this is result",result)
    return result
nums = [1,2,1]
print(maxelements(nums))
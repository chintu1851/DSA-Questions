def findpivot(nums):
    leftsum=0
    totalsum=sum(nums)
    for i in range(len(nums)-1):
        if (leftsum==totalsum-leftsum-nums[i]):
            return i
        leftsum+=nums[i]
    return -1
        
nums = [1,7,3,6,5,6]
print(findpivot(nums))
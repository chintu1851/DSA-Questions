def largestnumber(nums):
    maxnumber=max(nums)
    resultnum=0
    for result in range(len(nums)):
        if nums[result]==maxnumber:
            resultnum=result
            print(result)
        if nums[result]*2 >= maxnumber and nums[result]!=maxnumber:
            return -1
    return resultnum
nums = [0,0,0,1]
print(largestnumber(nums))
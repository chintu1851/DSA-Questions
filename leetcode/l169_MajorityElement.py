def majority(nums):
    nums.sort()
    currentcount=1
    maxvalue=1
    
    for i in range(len(nums)-1):
        print('i and i+1',nums[i],nums[i+1])
        if nums[i] == nums[i+1]:
            currentcount=currentcount+1
            maxvalue=max(maxvalue,currentcount)
        else:
            currentcount=1
    print(maxvalue)
nums = [2,2,1,1,1,2,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3]
majority(nums)
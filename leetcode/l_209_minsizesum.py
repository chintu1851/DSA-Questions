def minisizenum(target,nums):
    prefix=[0]*len(nums)
    prefix[0]=nums[0]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1]+nums[i]
        
    print(prefix)

target=7
nums=[2,3,1,2,4,3]

minisizenum(target,nums)
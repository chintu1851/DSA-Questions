def longestsubsequence(nums):
    count=1
    maxcount=1
    for i in range(len(nums)):
        if nums[i-1]<nums[i]:
            count+=1
            maxcount=max(maxcount,count)
        else:
            count=1
            maxcount=max(maxcount,count)
    print(maxcount)
nums = [1,3,5,4,2,3,4,5]
longestsubsequence(nums)
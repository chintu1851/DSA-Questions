def consecutiveones(nums):
    i=0
    j=len(nums)-1
    maxcount=0
    count=1
    if len(nums)==1 and nums[i]==1:
        return 1
    while i<j:
        print(i,i+1)
        # print(nums[i]==nums[i+1])
        if nums[i]&nums[i+1]==1:
            count+=1
            i+=1
        else:
            count=1
            i+=1
        maxcount=max(count,maxcount)
    return maxcount
nums = [1,1,0,1,1,1]
print(consecutiveones(nums))
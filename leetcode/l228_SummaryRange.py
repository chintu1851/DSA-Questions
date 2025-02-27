def sumamryrange(nums):
    l=[]
    i=0
    while i<len(nums):
        start=nums[i]
        while i<len(nums)-1 and nums[i]+1 == nums[i+1]:
            i+=1
        if start!=nums[i]:
            l.append(str(start)+'->'+str(nums[i]))
        else:
            l.append(str(start))
        i+=1
    return l
nums=[0,1,2,4,5,7]
print(sumamryrange(nums))
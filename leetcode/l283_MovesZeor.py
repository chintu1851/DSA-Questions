def movezero(nums):
    j=0
    i=0
    while(i<len(nums)):
        if nums[i]!=0:
            nums[i],nums[j] = nums[j],nums[i] 
            j+=1
        i+=1
    print(nums)
nums=[0,1,0,3,12]
movezero(nums)
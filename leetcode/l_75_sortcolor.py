def sortcolor(nums):
    print(nums)
    i = 0
    j= len(nums)-1
    
    while i < j:
        if nums[i]==0:
            nums[j] , nums[i] = nums[i] , nums[j]
            i+=1
            j-=1
        elif nums[i]<nums[j]:
            i+=1
            j-=1
            
    print(nums)
nums = [2,0,2,1,1,0]
sortcolor(nums)
def removeelement(nums,val):
    k=0
    
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            print(nums)
            k+=1
    print(k)
nums = [1,1,2,3,4]
val = 1
removeelement(nums,val)
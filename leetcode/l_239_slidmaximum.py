def slidemax(nums,k):
    left=0
    result=[]
    for left in range(len(nums)-k+1):
        val=max(nums[left:k])
        result.append(val)
        k+=1    
    print(result)
nums = [1,3,-1,-3,5,3,6,7]
k = 3
slidemax(nums,k)

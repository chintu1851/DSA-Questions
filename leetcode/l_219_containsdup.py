def containsdup(nums,k):
    
    count={}
    for i in range(len(nums)):
        if nums[i] in count and abs(i-count[nums[i]])<=k:
            print(count[nums[i]])
            return True
        count[nums[i]] = i
        print(count)
    return False
             
nums = [1,2,3,1]
k = 3
print(containsdup(nums,k))
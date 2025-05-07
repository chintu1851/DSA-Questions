def maxsubarr(nums, firstLen, secondLen):
    # Step 1: Calculate the max sum of any subarray of length firstLen
    
    currentsum=sum(nums[:firstLen])
    maxsum=currentsum
    for i in range(firstLen,len(nums)):
        currentsum+=nums[i]-nums[i-firstLen]
        maxsum=max(maxsum,currentsum)
        
    print(maxsum)
# Test input from the problem
nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2
maxsubarr(nums, firstLen, secondLen)

def maxsubarray(nums,k):
    windowsum=sum(nums[:k])
    avgvalue=windowsum
    for i in range(len(nums)-k):
        windowsum=windowsum-nums[i]+nums[i+k]
        avgvalue=max(avgvalue,windowsum)
    print(avgvalue/k)
        
nums = [1,12,-5,-6,50,3]
k=4
maxsubarray(nums,k)

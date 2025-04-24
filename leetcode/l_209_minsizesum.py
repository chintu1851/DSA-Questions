def minisizenum(target,nums):
    left=0
    sums=0
    minimal=float('inf')
    for right in range(len(nums)):
        sums+=nums[right]
        
        while sums>=target:
            minimal=min(minimal,right-left+1)
            sums-=nums[left]
            left+=1
    return 0 if minimal==float('inf') else minimal
target=7
nums=[2,3,1,2,4,3]

print(minisizenum(target,nums))
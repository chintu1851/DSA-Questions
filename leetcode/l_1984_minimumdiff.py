from itertools import combinations

def minimumdiff(nums, k):
        if len(nums)==1:
            return 0
        mindiff=float('inf')
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)-k+1):
            print((nums[i+k-1], nums[i]))
            currdiff=nums[i+k-1]-nums[i]
            mindiff=min(mindiff,currdiff)
        print(mindiff)
nums = [9,4,1,7] 
k= 3

minimumdiff(nums, k)

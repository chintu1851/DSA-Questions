def sumamryrange(nums):
    l=[]
    for i in range(1,len(nums)):
        result = 0
        result=nums[i]-nums[i-1]
        print(result)
        if result==1:
            l.append('nums[i]')
        else:
            l.append('')
    print(l)
nums=[0,1,2,4,5,7]
sumamryrange(nums)
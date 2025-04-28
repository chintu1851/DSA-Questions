def arithmetic(nums):
    if len(nums) < 3:
        return 0
    print(nums)
    result=0
    count=0
    difference=nums[1]-nums[0]
    for i in range(2,len(nums)):
        print("this is diff",difference)
        if nums[i]-nums[i-1]==difference:
            print('diff',difference)
            count+=1
            result+=count
            print("this is result",result)
        else:
            difference=nums[i]-nums[i-1]
            print(difference)
            count=0
    print(result)
nums=[1,3,4,6,8,10,12]
arithmetic(nums)

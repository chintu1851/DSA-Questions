def square(nums):
    left=0
    right=len(nums)-1
    result=[0]*len(nums)
    index = len(nums) - 1
    while left<=right:
        leftside=nums[left]*nums[left]
        rightside=nums[right]*nums[right]
        if leftside<rightside:
            result[index] = rightside
            right-=1
        else:
            result[index]=leftside
            left+=1
        index-=1
    print(result)
nums = [-7,-3,2,3,11]
square(nums)
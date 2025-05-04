def binarysearch(nums,goal):
    print(nums)
    checkgoal=0
    left=0
    count=1
    for right in range(len(nums)):
        checkgoal+=nums[right]
        while checkgoal>=goal:
            checkgoal-=nums[left]
            left+=1
            count+=1
    print(count)
    
nums = [0,0,0,0,0]
goal = 0

binarysearch(nums,goal)
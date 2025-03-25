def checkparity(nums):
    i=0
    j=1
    n=len(nums)-1
    while i<n and j<n:
        if nums[i] % 2 == 0:  # If even number is at even index, move forward
            i += 2
        elif nums[j] % 2 == 1:  # If odd number is at odd index, move forward
            j += 2
        else:
            # Swap the numbers at incorrect positions
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2  
    print(nums)    
nums = [4,2,5,7]
checkparity(nums)
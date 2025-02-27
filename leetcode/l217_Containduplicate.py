def containsDuplicate(nums,k):
    dicti = {}  # Dictionary to store element -> index mapping
    for num in range(len(nums)):  # Iterate over the full range
        if nums[num] in dicti:  # If number is already in the dictionary   
            pidx=dicti[nums[num]]
            print(pidx,num)
            if nums[pidx]==nums[num] and abs(pidx - num) <= k:
                return True
        dicti[nums[num]] = num  # Store the index instead of 1
    return False
k=1
nums = [1,0,1,1]
print(containsDuplicate(nums,k))

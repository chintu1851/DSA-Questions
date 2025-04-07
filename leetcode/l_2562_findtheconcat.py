def findconcat(nums):
    print(nums)
    i = 0
    j = len(nums) - 1
    value=0
    while i < j:
        print(int(str(nums[i]) + str(nums[j])))  # Fixed the issue here
        value = value+int(str(nums[i]) + str(nums[j]))
        i += 1
        j -= 1
    # print(value)
    if len(nums) % 2 != 0:
        print(nums[i])
        value = value + int(str(nums[i]))
        return value
    elif len(nums) % 2 == 0:
        return value
   
nums = [7,52,2,4]
print(findconcat(nums))
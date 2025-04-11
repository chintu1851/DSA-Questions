def sortcolor(nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zero = nums.count(0)
#         one = nums.count(1)
#         two = nums.count(2)
#         for i in range(zero):
#             nums[i] = 0
#         for i in range(zero, zero + one):
#             nums[i] = 1
#         for i in range(zero + one, len(nums)):
#             nums[i] = 2
#         print(nums)
# nums = [2,0,2,1,1,0]
# sortcolor(nums)

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    print(nums)

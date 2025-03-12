def parity(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] % 2 == 0:  # If even, move forward
            i += 1
        elif nums[j] % 2 != 0:  # If odd, move backward
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]  # Swap odd and even
            i += 1
            j -= 1

    print(nums)  # Output sorted by parity

nums = [2, 0, 3]
parity(nums)

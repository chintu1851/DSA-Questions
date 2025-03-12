def monotonic(nums):
        increasing = decreasing = True  # Assume both trends are possible

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False  # If increasing trend found, it's not decreasing
            elif nums[i] < nums[i - 1]:
                increasing = False  # If decreasing trend found, it's not increasing

            # Early exit optimization: If both are False, no need to continue
            if not increasing and not decreasing:
                return False
            print(nums[i],nums[i-1])
        return True  # If either flag is still True, it's monotonic

nums=[1,3,2]
print(monotonic(nums))
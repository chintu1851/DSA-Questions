def disappear(nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            print(index)
            nums[index] = -abs(nums[index])
            print(nums[index] )
        # Second loop: Collect missing numbers
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)
        return missing_numbers
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(disappear(nums))

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest_sum if this sum is closer to the target
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            # Move the pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If it's exactly equal, this is the closest possible
                return current_sum

    print(closest_sum)

# Example usage
nums = [0, 1, 2]
target = 0
threeSumClosest(nums, target)

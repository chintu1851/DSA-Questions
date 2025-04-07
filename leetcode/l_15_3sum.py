def sumcode(nums):
    # Step 1: Sort the input array
    nums.sort()
    
    # Step 2: Initialize an empty list to store the result
    result = []
    
    # Step 3: Iterate through the array
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Step 4: Use two pointers to find pairs that sum to -nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            # Step 5: Check if the sum is zero
            if total == 0:
                # Add the triplet to the result
                result.append([nums[i], nums[left], nums[right]])
                
                # Move pointers to skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers inward
                left += 1
                right -= 1
            elif total < 0:
                # If the sum is less than zero, move the left pointer to the right
                left += 1
            else:
                # If the sum is greater than zero, move the right pointer to the left
                right -= 1
    
    # Step 6: Print the result
    print("3Sum result:", result)

# Example input
nums = [-1, 0, 1, 2, -1, -4]
sumcode(nums)
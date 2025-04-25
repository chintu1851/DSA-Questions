# Function to find the minimal length of a contiguous subarray
# of which the sum is at least the given target
def minisizenum(target, nums):
    left = 0               # Left pointer of the sliding window
    sums = 0               # Variable to store the current sum of the window
    minimal = float('inf') # Initialize with infinity to track the minimal length

    # Loop through the array with the right pointer
    for right in range(len(nums)):
        sums += nums[right]  # Add current element to the window sum
        
        # While the current window sum is greater than or equal to target
        while sums >= target:
            # Update the minimal length if current window is smaller
            minimal = min(minimal, right - left + 1)
            # Shrink the window from the left
            sums -= nums[left]
            left += 1

    # If we never found a valid window, return 0. Otherwise, return the minimal length found.
    return 0 if minimal == float('inf') else minimal

# Example input
target = 7
nums = [2, 3, 1, 2, 4, 3]

# Output the result
print(minisizenum(target, nums))  # Output: 2

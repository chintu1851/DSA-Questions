def sliding_window_problem(arr, k):
    """
    Function to find the maximum sum of any contiguous subarray of size k 
    using the Sliding Window technique.

    Parameters:
    arr (list): List of integers
    k (int): Size of the subarray

    Returns:
    int: Maximum sum of any contiguous subarray of size k
    """
    
    # Edge case: If the array is empty or k is larger than the array size, return 0
    if not arr or k > len(arr):  
        return 0

    # Initialize variables to track the maximum sum and current window sum
    max_sum = 0  
    window_sum = 0  

    # Compute the sum of the first window (first k elements)
    window_sum = sum(arr[:k])
    max_sum = window_sum  # Initialize max_sum with the first window sum

    # Slide the window across the array
    for i in range(k, len(arr)):
        # Remove the first element of the previous window and add the next element
        window_sum += arr[i] - arr[i - k]

        # Update max_sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)

    return max_sum  # Return the maximum sum found

# Example input
arr = [2, 1, 5, 1, 3, 20]
k = 3

# Call the function and print the result
print(sliding_window_problem(arr, k))  # Expected Output: 24

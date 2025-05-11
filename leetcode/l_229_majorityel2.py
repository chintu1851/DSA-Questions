from collections import defaultdict

def majority(nums):
    # Step 1: Count the possible candidates using Boyer-Moore-like approach
    count = defaultdict(int)  # Dictionary to track the counts of each element
    
    # Initialize `newcount` before the loop to avoid UnboundLocalError
    newcount = defaultdict(int)
    
    # First pass - Find potential majority candidates (up to 2)
    for num in nums:
        count[num] += 1
        
        # If we have more than 2 candidates, reduce the counts
        if len(count) > 2:
            newcount = defaultdict(int)  # Reset newcount to avoid residual data
            for num, c in count.items():
                if c > 1:
                    newcount[num] = c - 1  # Decrease the counts of all elements by 1
            count = newcount  # Update the count with the reduced one
        print("First dict after processing", num, ":", count)
        print("Second dict after processing", num, ":", newcount)
        # Print the dictionaries after each iteration

    # Step 2: Verify the candidates by checking the actual counts in the original array
    res = []
    for num in count:
        if nums.count(num) > len(nums) // 3:  # Check if this candidate is a majority
            res.append(num)
    
    print("Majority elements:", res)

# Example input list
nums = [1,2,1,2,3,3,1,4]
majority(nums)

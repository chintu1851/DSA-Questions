def findShortestSubarray(nums):
    # Step 1: Count frequencies, and track first and last occurrence
    freq = {}
    first_occurrence = {}
    last_occurrence = {}
    
    for i, num in enumerate(nums):
        # Count frequency
        freq[num] = freq.get(num, 0) + 1
        # Track first occurrence
        if num not in first_occurrence:
            first_occurrence[num] = i
            # print('first',first_occurrence)
        # Track last occurrence
        last_occurrence[num] = i
        # print('last',last_occurrence)
        
    print(freq)
    # Step 2: Find the degree of the array (max frequency)
     
    degree = max(freq.values())
        
    # Step 3: Calculate the smallest length of subarray with the same degree
    min_length = float('inf')
    
    for num in freq:
        if freq[num] == degree:
            print(freq[num])
            subarray_length = last_occurrence[num] - first_occurrence[num] + 1
            print("s",subarray_length)
            min_length = min(min_length, subarray_length)
    
    print("min length",min_length)

nums = [1,2,2,3,3,3,1,4,2]
findShortestSubarray(nums)
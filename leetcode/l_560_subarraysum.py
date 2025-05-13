def subarraySum(nums, k):
    res = curSum = 0
    prefixSums = {0: 1}

    for num in nums:
        curSum += num
        diff = curSum - k

        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
    return res
print(subarraySum([1, 2, 3], 3))  # Output: 2
# Explanation: Subarrays [1,2] and [3]

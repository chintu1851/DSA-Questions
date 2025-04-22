def minPositiveSumSubarray(nums, l, r):
        n = len(nums)
        
        # Step 1: Build the prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print(prefix)
        minsum = float('inf')  # Initialize minsum to infinity

        # Step 2: Use the prefix sum to efficiently calculate subarray sums
        for size in range(l, r + 1):
            print('this is size',size)
            for i in range(n - size + 1):
                # print('size',i+size)
                curr_sum   = prefix[i + size] - prefix[i]
                print("prefixsumishere",prefix[i + size])
                if curr_sum > 0:
                    minsum = min(minsum, curr_sum)

        return minsum if minsum != float('inf') else -1
 
nums = [3, -2, 1, 4]
l = 2
r = 3
print(minPositiveSumSubarray(nums,l,r))
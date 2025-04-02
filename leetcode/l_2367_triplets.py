def triplets(nums,diff):
        seen = {}
        counter = 0
        for i in range(len(nums)):
            seen[nums[i]] = i
        for num in nums:
            if (num + diff) in seen and (num + 2 * diff) in seen:
                counter += 1
        return counter
nums = [0,1,4,6,7,10]
diff = 3
print(triplets(nums,diff))
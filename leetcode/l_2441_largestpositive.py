def largestnumber(nums):
    setnum = set(nums)  # O(n) space
    max_k = -1

    for num in nums:  # O(n) loop
        if num > 0 and -num in setnum:  # O(1) lookup in set
            max_k = max(max_k, num)

    return max_k
nums=[-1,10,6,7,-7,1]
print(largestnumber(nums))
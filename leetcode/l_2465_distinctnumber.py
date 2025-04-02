def distinct(nums):
    nums.sort()  # Sort the array first
    numset = set()  # Create an empty set
    while len(nums) > 1:
        minnum = nums.pop(0)  # Pop the first (smallest) element
        maxnum = nums.pop()  # Pop the last (largest) element
        avg = (minnum + maxnum) / 2
        numset.add(avg)
    print(nums)
    print(numset)
nums = [4, 1, 4, 0, 3, 5]
distinct(nums)

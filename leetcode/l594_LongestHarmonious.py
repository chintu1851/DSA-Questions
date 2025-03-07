from collections import Counter
def longestharmoinous(nums):
    freq = Counter(nums)  # Count occurrences of each number
    max_length = 0
    for num in freq:
        # print(num)
        # print(freq[num] )
        if num + 1 in freq:  # Check if (num, num+1) pair exists
            print(num)
            max_length = max(max_length, freq[num] + freq[num + 1])
            print(max_length)
    # print(freq)
nums = [1,3,2,2,5,2,3,7]
longestharmoinous(nums)
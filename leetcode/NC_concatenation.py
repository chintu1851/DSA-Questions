def concat_custom(nums):
    answer = []
    for i in range(len(nums)):
        answer.append(nums[i])
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            answer.append(nums[i])  # odd: at end (extra)
        else:
            answer.insert(i + len(nums), nums[i])  # even: at index + len(nums)
    print(answer)

nums = [1, 4, 1, 2]
concat_custom(nums)

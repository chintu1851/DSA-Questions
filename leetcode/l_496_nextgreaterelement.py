def nextgreaterelement(nums1,nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)
    for num in stack:
        next_greater[num]=-1
    result=[next_greater[num] for num in nums1]
    print(result)
nums1 = [4,1,2]
nums2 = [1,3,4,2]
nextgreaterelement(nums1,nums2)

def minisizenum(target,nums):
    l, s, m = 0, 0, float('inf')
    for r in range(len(nums)):
        s += nums[r]
        while s >= target:
            print("this is sum",s)
            print("inside loop",l)
            m = min(m, r - l + 1)
            s -= nums[l]
            l += 1

target=7
nums=[2,3,1,2,4,3]

minisizenum(target,nums)
def rotate(nums,k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

nums=[1,2,3,4,5,6,7,8]
k=3
rotate(nums,k)
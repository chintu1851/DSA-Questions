def consecutive(nums,k):
    left = 0
    counter = {0: 0, 1: 0}
    result = 0

    for right in range(len(nums)):
        counter[nums[right]] += 1

        while counter[0] > k:
            counter[nums[left]] -= 1
            left += 1

        result = max(result, right - left + 1)
    print(result)
        # l=r=0    
        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         k-=1
        #     if k<0:
        #         if nums[l] == 0:
        #             k+=1
        #         l+=1
        # return r-l+1
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
consecutive(nums,k)

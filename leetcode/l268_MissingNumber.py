def missingnumbers(nums):
    maxvalue=len(nums)
    # print(maxvalue)
    for i in range(len(nums)-1):
        if (maxvalue-i) not in nums:
            print(maxvalue-i)
nums=[1]
missingnumbers(nums)
        
        
    
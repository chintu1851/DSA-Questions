def product(nums):
    max1,max2,max3=float('-inf'),float('-inf'),float('-inf')
    min1,min2=float('inf'),float('inf')
    for num in nums:
        if num>max1:
            max1,max2,max3=num,max1,max2
        elif num>max2:
            max2,max3=num,max2
        else:
            max3=num
        if num<min1:
            min1,min2=num,min1
        else:
            min2=num
            
        product1=max1*max2*max3
        product2=min1*min2*max1
        product=max(product1,product2)
    
    print(product)
# Test case
nums = [-100, -2, -3, 1]
product(nums)

def smallestrange(nums,k):
    if not k and len(nums)==1:
        return 0
    mi=min(nums)+k
    mx=max(nums)-k
    if mi>mx:
        return 0
    else:
        return mx-mi

nums=[0,10]
k=2
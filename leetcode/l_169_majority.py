def majority(nums):
    count=0
    candidatevalue=0

    for num in nums:
        if count==0:
            candidatevalue=num
        if num==candidatevalue:
            count+=1
        else:
            count-=1
    print(candidatevalue)

nums = [5,5,1,1,1,5,5]
majority(nums)
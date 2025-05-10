from collections import defaultdict
def majority(nums):
    count=defaultdict(int)
    
    for num in nums:
        count[num]+=1
        
        if len(count)<2:
            continue
        
        newcount=defaultdict(int)
        for num,c in count:
            if c>1:
                newcount[num]=c-1
        count=newcount
        
        res=[]
        for num in count:
            if nums.count(num)>len(nums):
                res.append(num)
        print(res)
nums=[3,2,3,2,3,3,3,2]
majority(nums)
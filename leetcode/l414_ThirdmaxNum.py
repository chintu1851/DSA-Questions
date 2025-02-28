def thirdmax(nums):
    mylist=list(set(nums))
    if len(mylist)<3:
        return max(mylist)
    for _ in range(2):
        maxvalue=max(mylist)
        mylist.remove(maxvalue)
    print(max(mylist))
nums = [11,22,1,33,2,20]
thirdmax(nums)   

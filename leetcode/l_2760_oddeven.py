def oddeven(nums,threshold):
    result = []
    i=0
    j=len(nums)-1
    currnetlength=len(result)
    while i<j:
        print(nums[i])
        if((nums[i]%2==0 and nums[i]<threshold) and nums[i+1]%2!=0 and nums[i+1]<threshold):
            result.append(nums[i])
            result.append(nums[i+1])
            i+=1
        else:
            i+=1
            currnetlength=max(currnetlength,len(result))
            result=[]
    print(currnetlength)
nums = [3,2,5,4]
threshold = 5
oddeven(nums,threshold)
    
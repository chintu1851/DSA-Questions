def shifting(arr):
    temp=[]
    for i in arr:
        temp.append(i)
        if i==0 and len(temp)<len(arr):
            temp.append(0)
    for i in range(len(arr)):
        arr[i]=temp[i]
    print(arr)
arr = [1,0,2,3,0,4,5,0]
shifting(arr)
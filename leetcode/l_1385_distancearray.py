def distance(arr1,arr2,d):
    k=0
    i=0
    j=len(arr2)-1
    value=bool
    count=0
    while k<=len(arr1)-1 and i<=j:
        valeof=abs(arr1[k]-arr2[i]) 
        print(valeof)
        if valeof<=d:
            value=False
            k+=1
        else:
            value=True
            i+=1
        if (len(arr2)) == i:
            if value==True:
                count+=1
            k+=1
            i=0
        if k==len(arr1):
            print("this is count",count)      
arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(distance(arr1,arr2,d))
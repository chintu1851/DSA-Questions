def nextgreattest(letters,target):
    dicti={}
    target=ord(target)
    print(target)
    for i,value in enumerate(letters):
        if i not in dicti:
            dicti[i]=ord(value)
    newlist=list(dicti.values())
    print(newlist)
    result=newlist[0]
    low=0
    high=len(newlist)
    while low<high:
        mid=(low+high)//2
        if low==high:
            print(newlist[high])
        elif target<=newlist[mid]:
            high=mid
        else:
            low=mid+1
        print(low,high)
letters = ["c","f","j","k","l"]
target = "h"
nextgreattest(letters,target)
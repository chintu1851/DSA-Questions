def number(num,k):
    res=[]
    i=len(num)-1
    while i>=0 or k>0:
        if i>=0:
            k+=num[i]
            print(k)
        res.append(k%10)
        k//=10
        i-=1
    return res[::-1]
num = [2,1,5]
k = 806
print(number(num,k))

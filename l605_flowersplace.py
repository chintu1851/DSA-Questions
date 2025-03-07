def flowers(flowerbed,n):
    for i in range(len(flowerbed)-1):
        if (flowerbed[i] ^ flowerbed[i+1]==0 and flowerbed[i-1] ^ flowerbed[i]==1):
            print(i+1)
            n-=1
    if n==0:
        return True
    else:
        return False
flowerbed = [1,0,0,0,1]
n=2
print(flowers(flowerbed,n))
def capture(forts):
    i=0
    j=len(forts)
    k=0
    numset=set()
    newset=set()
    while i<j:
        if forts[i]== 1 or forts[j]==-1:
            if forts[i]==1:
                print(forts[i])
                numset.add(i)
            if forts[i]== -1:
                print(forts[i])
                newset.add(i)  
        elif forts[j]==1 or forts[j]==-1:
            if forts[j]==1:
                numset.add(j)
            if forts[j]==-1:
                newset.add(j)   
        i+=1
        j-=1
    print(numset)
    print(newset)
forts = [1,0,0,-1,0,0,0,0,1]
capture(forts)
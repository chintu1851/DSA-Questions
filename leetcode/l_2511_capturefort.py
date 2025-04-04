def capture(forts):
    ans=0
    prev=-1
    for i,fort in enumerate(forts):
        if fort!=0:
            if prev!=-1 and forts[prev]!=fort:
                ans=max(ans,i-prev-1)
            prev=i
    print(ans)
forts = [1,0,0,-1,0,0,0,0,1]
capture(forts)
def climbingstairs(cost):
    result=[]
    j=len(cost)-1
    if(len(cost)>=3):
        i=0
    else:
        i=1
    while i<j:
        if cost[i]<cost[i+1]:
            result.append(cost[i])
            i+=2
        else:
            result.append(cost[i])
            i+=1
    print(result)
    
cost = [10,15,20]
climbingstairs(cost)
def depthofparenthisis(s):
    count=0
    maxnum=0
    for i in s:
        print(count,maxnum)
        if i=='(':
            count+=1
            if count > maxnum:
                maxnum = count
        elif i==')':
            count-=1
    print(maxnum)
    
s = "(1+(2*3)+((8)/4))+1"
depthofparenthisis(s)
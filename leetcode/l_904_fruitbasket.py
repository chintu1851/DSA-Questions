def fruit(fruits):
    print(fruits)
    result=0
    dicti={}
    count=0
    left=0
    for i in range(len(fruits)):
        dicti[fruits[i]] = 1 + dicti.get(fruits[i],0)
        while len(dicti)>2:
            count+=1
            if dicti[fruits[i]]==0:
                del dicti[fruits[i]]
            left+=1
        result=max(result,i-left+1)
    print(result)
    
fruits = [1,2,1]
fruit(fruits)
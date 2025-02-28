def assigncookies(g,s):
    maxvalue=0
    sortchildren=sorted(g)
    sortcookies=sorted(s)
    chilindex=0
    cookiesindex=0
    while chilindex<len(sortchildren) and cookiesindex<len(sortcookies):
        if sortchildren[chilindex] <= sortcookies[cookiesindex]:
            maxvalue+=1
            cookiesindex+=1
            chilindex+=1
        cookiesindex+=1
    print(maxvalue)
g = [10, 20, 30]
s = [30, 30, 30, 20, 20]
assigncookies(g,s)

def distributeCandies(candyType):
    totalcandy=len(candyType)//2
    totaltype=len(set(candyType))
    if totalcandy>=totaltype:
        print(totaltype)
    else:
        print(totalcandy)
candyType= [1,1,2,2,3,3]
distributeCandies(candyType)
def validparenthisis(s):
    print(s)
    parenthisistack=[]
    starstack=[]
    
    for i in s:
        if i=='(':
            parenthisistack.append(i)
        elif i=='*':
            starstack.append(i)
        else:
            if parenthisistack:
                parenthisistack.pop()
            elif starstack:
                starstack.pop()
            else:
                return False
    # print(starstack)
    print(parenthisistack)
    
s = "()"
validparenthisis(s)

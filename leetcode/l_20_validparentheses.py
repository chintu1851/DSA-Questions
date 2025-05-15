def validparenthisis(s):
    dicti={'(':')', '{':'}','[':']' }
    stack=[]
    
    for i in range(len(s)):
        if s[i] in dicti.values():
            print(s[i])
        

    
        
s = "([{}])"
validparenthisis(s)
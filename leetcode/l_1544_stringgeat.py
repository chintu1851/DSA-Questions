def makestringgreat(s):
    
    print(s)
    strng=list(s)
    stack=[]
    for i in range(len(strng)):
        if stack and abs((ord(stack[-1])-ord(strng[i]))==32):
            stack.pop()
        else:
            stack.append(strng[i])
        
    print("".join(stack))    
s = "leEeetcode"
makestringgreat(s)


def removedigit(s):
    stack=[]
    for i in range(len(s)):
        if stack and s[i].isdigit():
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)
        
s="abc"
removedigit(s)
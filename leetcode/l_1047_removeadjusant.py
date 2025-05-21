def removeadjacent(s):

    print(s)
    stack=[]
    res=""
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    print("".join(stack))
    
s = "abbaca"
removeadjacent(s)
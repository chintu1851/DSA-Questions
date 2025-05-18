def evaluate(tokens):
    
    stack=[]
    for num in range(len(tokens)):
        if tokens[num]=="+":
            stack.append(stack.pop()+stack.pop())
        elif tokens[num]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        elif tokens[num]=="*":
            stack.append(stack.pop()*stack.pop())
        elif tokens[num]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(b/a)
        else:
            stack.append(tokens[num])
    print(stack)
tokens = ["2","1","+","3","*"]
evaluate(tokens)
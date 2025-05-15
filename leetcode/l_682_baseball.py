def baseball(ops):
    stack = []
    for num in range(len(ops)):
        if ops[num] == "+":
            stack.append(stack[-1] + stack[-2])
        elif ops[num] == "C":
            stack.pop()
        elif ops[num] == "D":
            stack.append(2 * stack[-1])
        else:
            stack.append(int(ops[num]))
    print(sum(stack))

ops = ["1", "2", "+", "C", "5", "D"]
baseball(ops)

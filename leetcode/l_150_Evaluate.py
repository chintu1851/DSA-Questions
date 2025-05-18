def evaluate(tokens):
    stack = []

    for tok in tokens:
        if tok == "+":
            stack.append(stack.pop() + stack.pop())

        elif tok == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)

        elif tok == "*":
            stack.append(stack.pop() * stack.pop())

        elif tok == "/":
            a = stack.pop()
            b = stack.pop()
            # truncate toward 0 (LeetCode spec); use int() on the float result
            stack.append(int(b / a))      

        else:  # operand
            stack.append(int(tok))        # <‑‑ convert to int here

    return stack[0]                      # final result

tokens = ["2", "1", "+", "3", "*"]
print(evaluate(tokens))   # → 9

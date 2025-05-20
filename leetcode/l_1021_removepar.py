def removeparenthesis(strs):
    stack1 = []
    res = ""

    for i in range(len(strs)):
        print(stack1)
        if strs[i] == '(':
            if stack1:  # Only add to result if it's NOT the outermost '('
                res += '('
            stack1.append('(')
        elif strs[i] == ')':
            stack1.pop()
            if stack1:  # Only add to result if it's NOT the outermost ')'
                res += ')'

    print(res)
    
strs = "(()())(())(()(()))"
removeparenthesis(strs)
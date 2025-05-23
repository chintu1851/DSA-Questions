def calculator(s):
    operators = {'+', '-', '/', '*'}
    currentsign = '+'
    currentnum = 0
    stack = []

    if not s:
        return 0

    nums = set(str(x) for x in range(10))

    for i in range(len(s)):
        char = s[i]

        if char in nums:
            currentnum = currentnum * 10 + int(char)

        if char in operators or i == len(s) - 1:
            if currentsign == '+':
                stack.append(currentnum)
            elif currentsign == '-':
                stack.append(-currentnum)
            elif currentsign == '*':
                stack[-1] = stack[-1] * currentnum
            elif currentsign == '/':
                stack[-1] = int(stack[-1] / currentnum)

            currentsign = char
            currentnum = 0

    print(sum(stack))

# Example run
s = " 3+5 / 2 "
calculator(s)  # Output: 5

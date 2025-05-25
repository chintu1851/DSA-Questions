def removedigit(num, k):
    stack = []
    for i in num:
        while stack and stack[-1] > i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    # Corrected the condition here
    while k > 0:
        stack.pop()
        k -= 1

    result = ''.join(stack).lstrip('0')
    print("Final Stack:", stack)
    print("Result after removing leading 0s:", result)
    return result if result else "0"

    
num = "123456"
k = 3
removedigit(num,k)
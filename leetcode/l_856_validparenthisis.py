def scoreofparenthisis(s):
    stack = []
    score = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(score)
            score = 0
        else:
            last = stack.pop()
            score = last + max(2 * score, 1)
        print(stack)
    return score


s = "(()(()))"
print(scoreofparenthisis(s))
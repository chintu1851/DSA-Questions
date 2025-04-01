def palindromic(words):
    print(words)
    for i in words:
        s=i[::-1]
        if i==s:
            return i
    return ""
words = ["abc","car","ada","racecar","cool"]
print(palindromic(words))
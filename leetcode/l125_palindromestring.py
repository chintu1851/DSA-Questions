def palindrome(s):
    news = "".join(char for char in s if char.isalnum()).lower()
    i, j = 0, len(news) - 1
        
    while i < j:
        if news[i] != news[j]:
            return False
        i += 1
        j -= 1

    return True
s = "0P"
print(palindrome(s))
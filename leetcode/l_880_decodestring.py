def decodestring(s, k):
    size=0
    # First, calculate the total size of the decoded string
    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        k %= size  # Reduce k within current size
        print(k,size)
        if k == 0 and char.isalpha():
            return char

        if char.isdigit():
            size //= int(char)
        else:
            size -= 1
    print(size)
# Test
s = "leet2code3"
k = 10
decodestring(s, k)

def rever(s):
    s = list(s)  # Convert string to a list
    i = 0
    j = len(s) - 1
    
    while i < j:
        if (s[i].isalpha() and s[j].isalpha()):
            s[i], s[j] = s[j], s[i]  # Swap characters
        i += 1
        j -= 1
    
    return "".join(s)  # Convert list back to a string

s = "a-bC-dEf-ghIj"
print(rever(s))  # Output: "dc-ba"

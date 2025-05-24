def removeduplicate(s):
    last_index = {char: i for i, char in enumerate(s)}  # Last occurrence
    print(last_index)
s="cbacdcbc"
print(removeduplicate(s))
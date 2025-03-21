def shortest(s,c):
    store=[float('inf')]*len(s)
    prev = float('-inf')
    for i in range(len(s)):
        if (s[i]==c):
            prev=i
        store[i]=abs(i-prev)
    prev = float('inf')
    print("this",prev)
    for i in range(len(s)-1,-1,-1):
        if (s[i]==c):
            prev=i
        store[i]=min(store[i],abs(i-prev))
    print(store)
    print(s)

s = "loveleetcode"
c = "e"
shortest(s,c)
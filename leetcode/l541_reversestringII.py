def reverses(s,k):
    i=0
    j=len(s)-1
    while i<j:
        s[i]=s[::-1]
        print(s)

s="abcde"
k=2
reverses(s,k)
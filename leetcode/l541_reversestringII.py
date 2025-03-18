def reverses(s,k):
        s = list(s)
        for i in range(0,len(s),2*k):
            # print(i)
            s[i:i+k] = reversed(s[i:i+k])
            print(i+k)
        return "".join(s)
s="abcde"
k=2
print(reverses(s,k))
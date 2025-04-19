from collections import defaultdict

def maxlength(s):
    d = defaultdict(int)  # Creates a default dictionary with default value of 0
    right=0
    left = 0
    Max = 0
    for i in s:
        right+=1
        d[i]+=1
        while d[i]>2:
            print(d[s[left]])
            d[s[left]]-=1
            left+=1
        Max=max(Max,right-left)
    print(d)
s = "bcbbbcba"
maxlength(s)

from collections import Counter
def longestsubstring(s,k):
    hashmap={}
    # print(c)
    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i],0)+1
    for j, value in enumerate(s):
        if hashmap[value]<k:
            left = longestsubstring(s[:i],k)
            right=longestsubstring(s[i+1:] ,k)
            return max(left,right)
    return len(s)
s = "aaabb"
k = 3
print(longestsubstring(s,k))

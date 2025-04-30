from collections import Counter

def anagrams(s,p):
    right=0
    left=0
    result=[]
    pcount=Counter(p)
    scount=Counter()
    for right in range(len(s)):
        scount[s[right]]+=1
        if (right-left+1)>len(p):
            scount[s[left]]-=1
            print(s[left])
            if scount[s[left]] == 0:
                del scount[s[left]]
                
            left += 1  
        if scount==pcount:
            print(scount)
            result.append(left)

    print(result)
s = "cbaebabacd"
p = "abc"
anagrams(s,p)
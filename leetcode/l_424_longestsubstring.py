def longestsub(s,k):
    left=0
    right=0
    count={}
    maxf=0
    result=0
    for right in range(len(s)):
        count[s[right]] = 1+count.get(s[right],0)
        maxf=max(maxf,count[s[right]])
        print((right-left+1)-maxf)
        while ((right-left+1)-maxf>k):
            print("inside")
            count[s[left]]-=1
            left+=1
            result=max(result,right-left+1)
    return result

s="ABAB"
k=1
print(longestsub(s,k))
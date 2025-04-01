def mergestring(word1,word2):
    l1=len(word1)
    l2=len(word2)
    i=0
    s=[]
    while i<min(l1,l2):
        s.append(word1[i]+word2[i])
        i+=1
    if i<l1:
        s.append(word1[i:])
    if i<l2:
        s.append(word2[i:])
        
    return "".join(s)
    
word1 = "abc"
word2 = "pqr"
print(mergestring(word1,word2))
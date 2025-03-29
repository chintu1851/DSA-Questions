def removestring(s):
    count=0
    print(s)
    if len(s)==0:
        return count
    if s==s[::-1]:
        count+=1
        print(count)
    i=0
    j=len(s)
    while i<j:
        
        
s = "abb"    
removestring(s)
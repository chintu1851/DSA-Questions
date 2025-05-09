def length(s):
    i=0
    j=len(s)-1
    
    while j>=0 and s[j]==" ":
        j-=1
    print(j)
    while j>=0 and s[j]!=" ":
        i+=1
        j-=1
    print(i)
s = "luffy is still joyboy"
length(s)
def longpress(name,typed):
    i=0
    j=0
    while j<len(typed):
        if i<len(name) and name[i]==typed[j]:
            i+=1
        elif j==0 or typed[j]!=typed[j-1]:
            return False
        j+=1
    return i == len(name)
name = "alex"
typed = "aaleex"
print(longpress(name,typed))
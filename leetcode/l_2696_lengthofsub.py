def minlength(s):
    
    print(s)
    res=''
    k=0
    updated=''
    i=0
    while i<len(s):
        if s[i:i+2]=="AB" or s[i:i+2]=="CD":
            i+=2
        else:
            updated+=s[i]
            i+=1
    print(updated)  
s="ABFCACDB"
minlength(s)
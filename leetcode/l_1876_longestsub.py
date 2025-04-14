def longeststr(s):
    counter=0
    for i in range(len(s)-2):
        charser = set(s[i:i+3])
        if len(charser)>2:
            counter+=1
    print(counter)
s = "xyzzaz"
longeststr(s)
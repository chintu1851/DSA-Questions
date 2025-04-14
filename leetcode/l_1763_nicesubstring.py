def longset(s):
    if len(s)<2:
        return ""
    charset=set(s)
    for i,st in enumerate(s):
        if st.swapcase() not in charset:
            leftside=longset(s[:i])
            rightside = longset(s[i+1:])
            return leftside if len(leftside)>len(rightside) else rightside
    return s
s='YazaAay'
print(longset(s))
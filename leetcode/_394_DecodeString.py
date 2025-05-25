def decodestring(s):
    
    stack=[]
    numstack=[]
    currentnum=0
    for char in s:
        if char.isdigit():
            currentnum=currentnum*10+int(char)
        elif char=='[':
            numstack.append(currentnum)
            currentnum=0
            stack.append(char)
        elif char==']':
            res=''
            while stack and stack[-1]!='[':
                res=stack.pop()+res
                print(res)
            stack.pop()
            count=numstack.pop()
            stack.append(count*res)         
        else:
            stack.append(char)
    print(numstack)
    print(stack) 
          
            

s = "3[a2[c]]"
decodestring(s)
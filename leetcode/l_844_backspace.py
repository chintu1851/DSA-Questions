def checkbackspace(s,t):
        stack1=[]
        stack2=[]
        
        for val in range(len(s)):
            stack1.append(s[val])
            if stack1 and s[val]=="#":
                stack1.pop()
        print(stack1)       
        for val in range(len(t)):
            stack2.append(t[val])
            if stack2 and t[val]=="#":
                stack2.pop()
                
        print(stack2)    
        return True if stack1==stack2 else False
    
s ="xywrrmp"
t ="xywrrmu#p"
print(checkbackspace(s,t))
def removeduplicate(s):
    last_index = {char: i for i, char in enumerate(s)}  # Last occurrence
    
    stack=[]
    seen=set()
    for i,char in enumerate(s):
        if char not in seen:
            
            while stack and char<stack[-1] and i<last_index[stack[-1]]:
                seen.remove(stack.pop())
            
            seen.add(char)
            stack.append(char)
                
        
    return "".join(stack)
s="cbacdcbc"
print(removeduplicate(s))
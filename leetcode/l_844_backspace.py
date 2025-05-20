def checkbackspace(s,t):
        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)
    
s ="xywrrmp"
t ="xywrrmu#p"
print(checkbackspace(s,t))
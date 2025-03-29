def removestring(s):
        # i, j = 0, len(s) - 1
        # while i <= j:
        #     if s[i] != s[j]:
        #         return 2
        #     i += 1
        #     j -= 1
        # return 1
        if s[::-1]==s:
            return 1
        
        return 2
        
s = "abb"    
print(removestring(s))
def checkprefix(s,words):
        merged = ""
        
        # Iterate through words and keep merging the strings
        for word in words:
            merged += word  # Add word to the merged string
            print(merged)
            if merged == s:  # If the merged string matches s, it's a prefix
                return True
        
        return False 
s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
print(checkprefix(s,words))
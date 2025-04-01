def revprefix(word,ch):
        place = ""  
        for i in range(len(word)):
            place += word[i]
            if word[i] == ch:  # Stop when 'ch' is found
                return place[::-1] + word[i+1:]  # Reverse prefix and append remaining
        return word
word = "abcd"
ch = "z"
print(revprefix(word,ch))
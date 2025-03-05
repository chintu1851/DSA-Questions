def keyboardctivity(words):
    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')

    result = []
        
    for word in words:
        lower_word = word.lower()  # Use a separate variable for lowercase comparison
        if all(char in row1 for char in lower_word):
            result.append(word)  # Append original word
        elif all(char in row2 for char in lower_word):
            result.append(word)
        elif all(char in row3 for char in lower_word):
            result.append(word)
        
    return result

strn = ["Hello","Alaska","Dad","Peace"]
print(keyboardctivity(strn))
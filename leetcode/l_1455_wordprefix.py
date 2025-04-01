def findword(sentence, searchWord):
        s = sentence.split()
        print("Words in sentence:", s)  # Debugging step

        for i in range(len(s)):  # Iterate through each word in the sentence
            if s[i].startswith(searchWord):  # Check if word starts with searchWord
                print("Index:", i + 1)  # Return index (1-based)
                return i + 1  

        print("Not Found")
        return -1  # Return -1 if not found

sentence = "i love eating burger"
searchWord = "burg"
findword(sentence, searchWord)

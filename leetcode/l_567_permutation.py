from collections import Counter
def permutationofstring(s1, s2):
    s1_freq = [0] * 26
    s2_freq = [0] * 26
    print("order",ord('e'))
    for char in s1:
        s1_freq[ord(char) - ord('a')] += 1

    for j in range(len(s2)):
        s2_freq[ord(s2[j]) - ord('a')] += 1

        if j >= len(s1):
            print(ord(s2[j - len(s1)])) 
            s2_freq[ord(s2[j - len(s1)]) - ord('a')] -= 1
        if s1_freq == s2_freq:
            return True

    return False

# Test
s1 = "ab"
s2 = "eidaboaoo"
print(permutationofstring(s1, s2))  # Output: True

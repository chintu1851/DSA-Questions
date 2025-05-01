from collections import Counter

def anagrams(s,p):
    # right=0
    # left=0
    # result=[]
    # pcount=Counter(p)
    # scount=Counter()
    # for right in range(len(s)):
    #     scount[s[right]]+=1
    #     if (right-left+1)>len(p):
    #         scount[s[left]]-=1
    #         print(s[left])
    #         if scount[s[left]] == 0:
    #             del scount[s[left]]
                
    #         left += 1  
    #     if scount==pcount:
    #         print(scount)
    #         result.append(left)
        if len(p) > len(s):
            return []

        result = []
        # Frequency arrays for 26 lowercase English letters
        p_freq = [0] * 26
        s_freq = [0] * 26

        for char in p:
            p_freq[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            s_freq[ord(s[i]) - ord('a')] += 1

            # Maintain the window size equal to len(p)
            if i >= len(p):
                s_freq[ord(s[i - len(p)]) - ord('a')] -= 1

            # Compare the two frequency arrays
            if s_freq == p_freq:
                print(p_freq)
                result.append(i - len(p) + 1)

        return result
s = "cbaebabacd"
p = "abc"
print(anagrams(s,p))
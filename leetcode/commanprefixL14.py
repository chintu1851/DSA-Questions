from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)  # Sort the list lexicographically
        first = v[0]  # The first string in the sorted list
        last = v[-1]  # The last string in the sorted list
        print(v)
        # Loop through characters of the first and last string
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:  # If characters don't match, return the current answer
                return ans
            ans += first[i]  # Add matched character to the answer
        
        return ans  # Return the longest common prefix

# Example usage
solution = Solution()
print(solution.longestCommonPrefix(["flowermy", "foolowermy", "flowermyght"]))  # Output: "fl"
print(solution.longestCommonPrefix(["cardogcar", "cracecar", "car"]))  # Output: ""

def strstr(haystack, needle):
    if not needle:  # Edge case: If needle is empty, return 0
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):  # Loop through haystack
        if haystack[i:i + m] == needle:  # Check if substring matches needle
            print(haystack[i:i + m])
            return i  # Return starting index
    
    return -1  # Return -1 if no match found

# Example usage:
haystack = "sabbutsad"
needle = "sad"
print(strstr(haystack, needle))  # Output: 6

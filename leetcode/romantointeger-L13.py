def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    print(roman_dict['V'])
    for i in range(len(s)):
        print(len(s))
        # Check if the current value is smaller than the next value (subtraction case)
        if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            result -= roman_dict[s[i]]  # Subtract the value
        else:
            result += roman_dict[s[i]]  # Add the value

    return result

# Test cases
# print(romanToInt("III"))    # 3
print(romanToInt("IV"))     # 4
# print(romanToInt("IX"))     # 9
# print(romanToInt("LVIII"))  # 58
# print(romanToInt("MCMXCIV"))  # 1994

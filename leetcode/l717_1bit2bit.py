def bitcheck(bits):
    i = 0
    j = len(bits)-1
    
    # Iterate through the bits array
    while i < j:
        if bits[i] == 1:
            # Check if it's followed by a valid second bit to form 10 or 11
            if i + 1 < j and bits[i + 1] in [0, 1]:
                i += 2  # Skip the next bit as it's part of the two-bit character
            else:
                return False  # Invalid sequence if the next bit is missing or incorrect
        else:
            i += 1  # Move to the next bit if it's a one-bit character (0)
    
    return True

# Test cases
bits = [1, 1, 1, 0]
print(bitcheck(bits))  # Output: False

bits = [1, 0, 0]
print(bitcheck(bits))  # Output: True

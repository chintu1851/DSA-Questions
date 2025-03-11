from collections import Counter

def shortestWord(licensePlate, words):
    # Extract only alphabetic characters and convert them to lowercase
    license_filtered = "".join([char for char in licensePlate if char.isalpha()]).lower()
    
    # Count the occurrences of characters in the license plate
    license_counter = Counter(license_filtered)

    # Initialize shortest word variable
    shortest = None

    # Iterate over words
    for word in words:
        word_counter = Counter(word)

        # Check if all required letters are present in the word
        if all(word_counter[char] >= license_counter[char] for char in license_counter):
            if shortest is None or len(word) < len(shortest):
                shortest = word  # Update shortest word
    
    return shortest  # Return the shortest matching word

# Example Usage
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(shortestWord(licensePlate, words))  # Output: "step"

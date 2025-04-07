# Two-pointer approach
def twosum2_two_pointer(numbers, target):
    result = []
    left = 0
    right = len(numbers) - 1
    while left < right:
        sums = numbers[left] + numbers[right]
        if sums == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif target > sums:
            left += 1
        else:
            right -= 1
    return []  # Return an empty list if no solution is found

# Dictionary-based approach
def twosum2_dict(numbers, target):
    numsdict = {}
    for i, num in enumerate(numbers):
        component = target - num
        if component in numsdict:
            return [numsdict[component] + 1, i + 1]  # Return 1-based indices
        numsdict[num] = i
    return []  # Return an empty list if no solution is found

numbers = [2, 7, 11, 15]
target = 9

# Example usage
print(twosum2_two_pointer(numbers, target))  # Using two-pointer approach
print(twosum2_dict(numbers, target))  # Using dictionary-based approach
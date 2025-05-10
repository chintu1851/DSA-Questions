def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = mergeSort(arr[:mid])
    rightHalf = mergeSort(arr[mid:])

    return merge(leftHalf, rightHalf)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two halves into result[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

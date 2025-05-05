# one approach in which space complexity is n2 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



# ------------------better approach in which space complexity is n-------------------
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Recursively sort the left and right halves
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    # Merge the sorted halves back into arr
    mergeInPlace(arr, leftHalf, rightHalf)

    return arr

def mergeInPlace(arr, left, right):
    i = j = k = 0  # i -> index for left, j -> index for right, k -> index for arr

    # Merge elements into the original array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
mergeSort(unsortedArr)
print("Sorted array:", unsortedArr)

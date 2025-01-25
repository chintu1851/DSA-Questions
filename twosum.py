# we are using two pointer approach for this problem

def twopointer(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left<right:

        sum = arr[left] + arr[right]

        if sum == target:
            return (arr[left],arr[right])
        
        elif sum < target:
            left = left+1
        else:
            right = right - 1

    return False

arr = [2, 4, 11, 56, 11]
target = int(input("Enter target sum: "))  # Convert input to an integer
result = twopointer(arr, target)
print(result)
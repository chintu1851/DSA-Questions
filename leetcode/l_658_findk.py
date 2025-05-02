def findk(arr,k,x):
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            print(x - arr[mid],arr[mid + k] - x)
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

arr = [1,2,3,4,5]
k = 4
x = 3
findk(arr,k,x)
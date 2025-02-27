def singlenumber(arr):
    result=0
    for i in range(len(arr)):
        result^=arr[i]
    return result
arr=[2,2,1]
print(singlenumber(arr))
def digits(nums):
    result = int("".join(map(str, nums)))
    print(result)
    result = result+1
    print(list(map(int, str(result))))
    return list(map(int, str(result)))
            
# Input List
nums = [1,3,5]
print(digits(nums))

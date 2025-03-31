def checkIfExist(arr):
        arr_set = set(arr)  # Convert arr to a set for O(1) lookups
        dicti = {}
        doublearray = [num * 2 for num in arr]

        for num in doublearray:
            if num == 0:
                # Special case for zero: we need at least two zeros
                if arr.count(0) > 1:
                    return True
            elif num in arr_set:
                return True  # If double exists in arr_set, return True

        return False  # No valid pair found

arr = [10, 2, 5, 3]
checkIfExist(arr)
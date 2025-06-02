def maxchunk(arr):
        ans = 0
        prev_max = 0
        for idx, x in enumerate(arr):
            prev_max = max(prev_max, x)
            print("prevmacx",prev_max)
            if prev_max == idx:
                print('this is idx',idx)
                ans += 1
        return ans

arr = [1,0,2,3,4]
print(maxchunk(arr))
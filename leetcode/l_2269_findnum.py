def beautynum(num, k):
    print(num)
    nums = str(num)
    counter = 0
    for i in range(len(nums) - k + 1):
        newnum = nums[i:i + k]  # 👈 take full substring of length k
        print(newnum)
        if int(newnum) != 0 and num % int(newnum) == 0:
            counter += 1
    print(counter)
num=765
k=3
beautynum(num,k)
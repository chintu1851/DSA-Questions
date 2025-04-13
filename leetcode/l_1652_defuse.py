def decrypt(code, k):
    n = len(code)
    for i in range(n):
        if k < 0:
            result = [code[(i + k + j) % n] for j in range(abs(k))]
            print(f"i = {i}, value = {code[i]} → previous {abs(k)}:", result)
        elif k > 0:
            result = [code[(i + 1 + j) % n] for j in range(k)]
            print(f"i = {i}, value = {code[i]} → next {k}:", result)
        else:
            print(f"i = {i}, value = {code[i]} → No elements to show (k = 0)")

code = [5,7,1,4]
k = -2
decrypt(code,k)
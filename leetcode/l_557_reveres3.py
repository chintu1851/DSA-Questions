def reverese(s):
    x=s.split()
    print(x)
    y=" ".join(char[::-1] for char in x)
    print(y)
s="Let's take LeetCode contest"
reverese(s)
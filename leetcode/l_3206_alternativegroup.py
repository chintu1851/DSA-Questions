def alternative(colors):
    count=0
    n=len(colors)
    for i in range(len(colors)):
        a=colors[i]
        b=colors[(i+1) % n]
        c=colors[(i+2) % n]
        print((i+1) % n,(i+2) % n)
        if c==a and b!=a:
            count+=1
    print(count)
  

colors = [0, 1, 0, 0, 1]
alternative(colors)


def primenumber(n):
    temp = []
    if n==0 or n==1:
        return False
    for i in range(2,int((n**0.5)+1)):
        if i%2 ==0:
            temp.append(i)
        else:
            continue
    return temp

          
    
primenumber(100)
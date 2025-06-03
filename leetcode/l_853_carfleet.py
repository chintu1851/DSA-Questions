def carfleet(target,position,speed):
    sets={}
    p=len(position)
    s=len(speed)
    i=0
    j=0
    while i<=s and j<=p:
        fleet=(target-position[j])/speed[i]
        
        print(fleet)
        i+=1
        j+=1
    print(fleet)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
carfleet(target,position,speed)
def carfleet(target, position, speed):
    # Step 1: Pair positions and speeds and sort by position (descending)
    cars = sorted(zip(position, speed), reverse=True)
    print(cars)
    stack = []  # This will store fleet arrival times
    
    i = 0
    while i < len(cars):
        pos, spd = cars[i]
        # print(pos,spd)
        time = (target - pos) / spd
        print("this is time",time)
        # If stack is empty or current car takes longer, it forms a new fleet
        
        if not stack or time > stack[-1]:
            
            stack.append(time)
            print(stack[-1])
            
        # else: the car merges into a fleet, so don't add to stack

        i += 1
    print(len(stack))

target = 12
position = [10, 8, 0, 5, 3]
speed    = [2,  4, 1, 1, 3]
carfleet(target, position, speed)

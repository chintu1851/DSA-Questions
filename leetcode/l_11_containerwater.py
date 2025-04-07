def container(height):
    print(height)
    left=0
    right=len(height)-1
    max_area=0
    while left<right:
        width=right-left
        print("width",width)
        max_area=max(max_area,width*min(height[left],height[right]))
        print("max_area",max_area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    print(max_area)
height=[1,8,6,2,5,4,8,3,7]
container(height)
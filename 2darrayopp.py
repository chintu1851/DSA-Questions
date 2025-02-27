from array import *
def findin2d(matrix,target):
    for i in range(len(matrix)):
        l=0
        r=len(matrix[i])-1
        # print(j)
        while l<=r:
           mid=(l+r)//2
           if matrix[i][mid]==target:
               return True
           elif matrix[i][mid]<target:
               l=mid+1
           else:
               r=mid-1
    return False
            
target=2222
matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
print(findin2d(matrix,target))
        

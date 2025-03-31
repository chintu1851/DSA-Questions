def distance(arr1, arr2, d):
        arr2_sorted = sorted(arr2)  # O(m log m)
        count = 0
        
        # # For each element in arr1
        # for num in arr1:  # O(n)
        #     # Binary search to find leftmost position where arr2 element could be within d
        #     left = 0
        #     right = len(arr2_sorted) - 1
            
        #     # Check if any element exists within distance d
        #     has_close = False
        #     while left <= right:  # O(log m)
        #         mid = (left + right) // 2
        #         if abs(num - arr2_sorted[mid]) <= d:
        #             has_close = True
        #             break
        #         elif arr2_sorted[mid] < num:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
                    
        #     if not has_close:
        #         count += 1
                
        # return count       
        for num in arr1:
            left=0
            right=len(arr2_sorted)-1
            close = False
            while left<=right:
                mid=(right+left)//2
                if abs(arr2_sorted[mid]-num)<=d:
                    close = True
                    break
                elif arr2_sorted[mid]<num:
                    left=mid+1
                else:
                    right=mid-1
                    
            if not close:
                count+=1
        return count
            
# Test Case
arr1 = [1, 4, 2, 3]
arr2 = [-4, -3, 6, 10, 20, 30]
d = 3

print(distance(arr1, arr2, d))  # Outputs: 2
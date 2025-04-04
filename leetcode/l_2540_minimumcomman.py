def minimumcommn(nums1,nums2):
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]==nums2[j]:
            return nums1[i]
        elif nums1[i]<nums2[j]:
            i+=1
        else:
            j+=1
            
    return -1
nums1 = [2,4]
nums2=[1,2]
print(minimumcommn(nums1,nums2))

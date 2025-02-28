# def intersection(nums1,nums2):
#     newset=set(nums2)
#     result=set()
#     for num in nums1:
#         if num in newset:
#             result.add(num)
#     return list(result)
# nums1=[4,9,5]
# nums2=[9,4,9,8,4]
# print(intersection(nums1,nums2))
def intersection2(nums1,nums2):
    result=[]
    if len(nums1)<len(nums2):
        newset=set(nums2)
    else:
        newset=set(nums1)
    if len(nums1)<=len(nums2):
        newlength=nums1
    else:
        newlength=nums2
    for num in newlength:
        if num in newset:
            result.append(num)
    return result
nums1=[3,1,2]
nums2=[1,1]
print(intersection2(nums1,nums2))


def distance(arr1, arr2, d):
    k = 0
    i = 0
    j = len(arr2) - 1
    count = 0
    value = True  # Proper initialization of value

    while k <= len(arr1) - 1 and i <= j:
        if abs(arr1[k] - arr2[i]) <= d:
            value = False  # Found a close element, mark as False
            k += 1  # Move to the next element in arr1
            i = 0  # Reset i to start checking from the beginning of arr2
        else:
            i += 1  # Move to the next element in arr2

        if i == len(arr2):  # If we have checked all elements of arr2
            if value:  # If no element in arr2 satisfied the condition
                count += 1
            k += 1  # Move to the next element in arr1
            i = 0  # Reset i for the next arr1 element
            value = True  # Reset value for the next check

    return count  # Return the final count

# Test Case
arr1 = [-803, 715, -224, 909, 121, -296, 872, 807, 715, 407, 94, -8, 572, 90, -520, -867, 485, -918, -827, -728, -653, -659, 865, 102, -564, -452, 554, -320, 229, 36, 722, -478, -247, -307, -304, -767, -404, -519, 776, 933, 236, 596, 954, 464]
arr2 = [817, 1, -723, 187, 128, 577, -787, -344, -920, -168, -851, -222, 773, 614, -699, 696, -744, -302, -766, 259, 203, 601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766, -63, 836, -433, -780, 611, -907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919, -616, -510, 608, 201, -138, -669, -764, -77, -658, 394, -506, -675, 523, 730, -790, -109, 865, 975, -226, 651, 987, 111, 862, 675, -398, 126, -482, 457, -24, -356, -795, -575, 335, -350, -919, -945, -979, 611]
d =37

print(distance(arr1, arr2, d))  # Expected output based on logic

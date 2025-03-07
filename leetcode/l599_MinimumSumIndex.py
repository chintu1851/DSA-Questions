from collections import Counter

def minsum(list1, list2):
    dicti1 = Counter(list1)
    dicti2 = {}
    minindex = float('inf')
    result = []

    for i in range(len(list2)):
        if list2[i] in dicti1:
            dicti2[list2[i]] = i  # Store index of common elements in list2

    print(dicti2)

    for j in range(len(list1)):      
        if list1[j] in dicti2:
            index_sum = dicti2[list1[j]] + j
            print(index_sum)
            if index_sum < minindex:
                minindex = index_sum
                result = [list1[j]]
            elif index_sum == minindex:
                result.append(list1[j])

    print(result)

list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]

minsum(list1, list2)

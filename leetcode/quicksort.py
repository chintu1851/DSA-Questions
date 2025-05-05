
def partition(arrayelement,low,high):
    pivot=arrayelement[high]
    idx=low-1
    for j in range(low,high):
        if(arrayelement[j]<=pivot):
            idx=idx+1
            (arrayelement[idx],arrayelement[j])=(arrayelement[j], arrayelement[idx])
    
    (arrayelement[idx+1],arrayelement[high])=(arrayelement[high],arrayelement[idx+1])

    return idx+1

def quicksort(arrayelement,low,high):
    if low<high:
        pi = partition(arrayelement,low,high)
        quicksort(arrayelement,low,pi-1)
        quicksort(arrayelement,pi+1,high)

arrayelement=[20,2,34,33,44,55,61,23]
print("this is unsorted array",arrayelement)
low=0
high=len(arrayelement)
quicksort(arrayelement,0,high-1)
print("this is sorted array",arrayelement)

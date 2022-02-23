# Merge Sort 
# Divide and Conquer--> keep dividing an array into parts and sort the parts, finally merge the sorted parts
# Time Complexity = O(n logn)
# Space Complexity = O(n)

def merge(arr, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        L = arr[0: n//2]
        R = arr[n//2: ]
        merge_sort(L)
        merge_sort(R)
        merge(arr, L, R)
    return arr
    


arr = [5, 2, 4, 6, 1, 3]
print(merge_sort(arr))
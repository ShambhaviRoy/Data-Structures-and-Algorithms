# Insertion Sort algorithm
# Time Complexity = O(n^2)
# Space Complexity = O(1)

def insertion_sort(arr):
    n = len(arr)

    for j in range(1, n):
        # arr[0:j-1] is the sorted part of the array
        key = arr[j]
        i = j - 1
        
        # key is compared with every element in the sorted part 
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

    return arr


arr = [5, 2, 4, 6, 1, 3]
print(insertion_sort(arr))

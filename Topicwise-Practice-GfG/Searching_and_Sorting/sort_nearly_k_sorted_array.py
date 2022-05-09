# Sort a nearly sorted (k sorted) array
# Each element in input is k steps away from its actual position in sorted output

# Input: arr = [6, 5, 3, 2, 8, 9, 10], k = 3
# Output: arr = [2, 3, 5, 6, 8, 9, 10]

# Approach 1: Use Insertion Sort
# Time Complexity = O(nk)

def insertion_sort(arr, k):
    i, j, key = 0, 0, 0

    for i in range(k):
        key = arr[i]
        j = i - 1

        # move elements in arr[0,.., i-1] greater than key to one position right
        # this loop runs at most k times
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


arr = [6, 5, 3, 2, 8, 9, 10]
k = 3
print(arr)
print('Sorted arr:', insertion_sort(arr, k))
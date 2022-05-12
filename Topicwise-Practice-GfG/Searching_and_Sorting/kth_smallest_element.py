# To find kth smallest element in unsorted array

# Approach 1: Sort array and return element at index k-1
# Time Complexity = O(n log n)

# Approach 2: Quick Select
# Pick a pivot and use it to partition the sequence
# Check if the position of pivot is k, if true then return element at that position

import sys

def partition(arr, start, end):
    x = arr[end]
    i = start

    for j in range(start, end):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


def kth_smallest(arr, k, start, end):
    if k > 0 and k <= end - start + 1:
        pivot = partition(arr, start, end)          # pick a pivot 

        if pivot - start == k - 1:
            return arr[pivot]

        if pivot - start > k - 1:
            return kth_smallest(arr, k, start, pivot-1)               # recur for left subarray

        return kth_smallest(arr, k, pivot+1, k-pivot+start-1)

    return sys.maxsize



arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
n = len(arr)
print(kth_smallest(arr, k, 0, n-1))

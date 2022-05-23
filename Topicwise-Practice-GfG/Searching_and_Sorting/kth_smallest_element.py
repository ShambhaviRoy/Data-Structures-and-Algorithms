# To find kth smallest element in unsorted array

# Approach 1: Sort array and return element at index k-1
# Time Complexity = O(n log n)

# Approach 2: Quick Select
# Pick a pivot and use it to partition the sequence
# Check if the position of pivot is k, if true then return element at that position

# Time Complexity:
# Worst Case = O(n^2), Average (Expected) Case = O(n)

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
    if start == end:
        return arr[start]
    
    if (k > 0 and k <= end - start + 1):
        # pivot_index = partition(arr, start, end)  # to pick a pivot

        pivot_index = random_partition(arr, start, end) # to pick random pivot

        if pivot_index - start == k - 1:
            return arr[pivot_index]

        if pivot_index - start > k - 1:
            return kth_smallest(arr, k, start, pivot_index - 1)
        
        return kth_smallest(arr, k - pivot_index + start - 1, pivot_index + 1, end)
        


# Approach 3: Randomized Quick Select
# Pick a pivot at random and swap the end element with the element at pivot index
# Quick Select procedure remains same

# Time Complexity:
# Worst Case = O(n^2), Average (Expected) Case = O(n)

import random

def random_partition(arr, start, end):
    n = end - start + 1
    pivot_index = random.randint(start, end)
    # swap with end element
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return partition(arr, start, end)




# Test Case
arr = [10, 4, 5, 8, 6, 11, 26]
k = 3
n = len(arr)
print(kth_smallest(arr, k, 0, n-1))
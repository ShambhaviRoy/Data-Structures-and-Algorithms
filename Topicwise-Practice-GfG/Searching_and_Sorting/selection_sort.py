# Selection Sort
# Find minimum element in section of arr and put it in front
# First subarray is sorted, other one unsorted
# In every iteration, every element from the unsorted subarray is put in the sorted subarray

# Time Complexity = O(n^2), Space Complexity = O(1) --> in-place algorithm


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            # print(i, min_index, j, arr)
        # swap arr[min_index] and arr[i]
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


# Stable sort ensures that two objects with equal or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        key = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1
        arr[i] = key

    return arr



# arr = [64, 25, 12, 22, 11]
arr = [4, 5, 3 , 2, 1, 4]
print('Original Array:', arr)
sorted_arr = selection_sort(arr)
stably_sorted_arr = stable_selection_sort(arr)
print('Sorted Array:', sorted_arr)
print('Stably sorted array:', stably_sorted_arr)

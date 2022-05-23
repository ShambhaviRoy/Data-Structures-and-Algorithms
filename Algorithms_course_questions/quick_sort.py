# Quick Sort Algorithm
# Select a pivot index and partition the array. Elements on left of the pivot are lesser than pivot and elements on the right of pivot are greater than pivot.
# Then the parts are sorted --> done recursively.

# Time Complexity = O(n^2) in worst case

def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
            arr[start], arr[end] = arr[end], arr[start]
        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end


def quick_sort(start, end, arr):
    if start < end:
        # partition arr into 2 parts: all no.s less than pivot and all no.s greater than pivot
        i = partition(start, end, arr)
        quick_sort(start, i, arr)
        quick_sort(i+1, end, arr)

    return arr

arr = [5, 2, 4, 6, 1, 3]
print(quick_sort(0, len(arr)-1, arr))
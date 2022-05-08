# Bubble Sort
# Compare adjacent elements and swap them if they aren't in order
# The algorithm needs one whole pass without any swaps to know that the input is sorted
# Optimization - stop when there is no swap

# Time Complexity = O(n^2)


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                # swap
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        if swapped == False:
            break

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
ans = bubble_sort(arr)
print(ans)
# Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
# integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
# array of integers, sort the array into an alternating sequence of peaks and valleys.
# EXAMPLE
# Input: {5, 3, 1, 2, 3}
# Output: {5, 1, 3, 2, 3}

# Time complexity = O(N log N)
def peak_valley_sort1(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)-1, 2):
        arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


# Time complexity = O(N)
def peak_valley_sort2(arr):
    for i in range(1, len(arr)-1, 2):
        # swap current element with the bigger adjacent element
        max_index = arr.index(max(arr[i-1], arr[i], arr[i+1]))
        # swap
        if i != max_index:
            arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr


arr = [5, 3, 1, 2, 3]
print(peak_valley_sort1(arr))
print(peak_valley_sort2(arr))

        

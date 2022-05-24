# Sort an array into a wave
# An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..


# Approach 1: Sort and swap adjacent elements
# Time Complexity = O(n log n)
def wave(arr):
    n = len(arr)
    arr.sort()

    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# Approach 2: Array traversal (ensure that all even position elements are greater than elements in odd positions)
# Traverse even positions in the array
# If the prev even position element < odd element, swap(prev, current)
# If the current element is smaller than the next odd element, swap next and current
def wave2(arr):
    n = len(arr)
    for i in range(0, n-1, 2):
        # if current element is smaller than the next odd element, swap next and current
        if i > 0 and arr[i] < arr[i-1]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        
        # If the prev even position element < odd element, swap(prev, current)
        if i < n-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


arr = [3, 6, 5, 10, 7, 20]
print(arr)
print(wave(arr))
print(wave2(arr))
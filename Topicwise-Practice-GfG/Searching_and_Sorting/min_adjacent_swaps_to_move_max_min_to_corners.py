# Minimum adjacent swaps to move maximum and minimum to corners
# Find the index of the maximum and minimumm element in arr
# Generally, swaps = max_index + (n - min_index -1)
# But if max_index > min_index, 1 swap is already performed to bring the maximum towards the front

# Time Complexity = O(n)


def find_min_swaps(arr):
    n = len(arr)
    minimum,maximum = arr[0], arr[0]
    min_index, max_index = 0, 0
    
    for i in range(n):
        if arr[i] <= minimum:
            minimum = arr[i]
            min_index = i

        if arr[i] > maximum:
            maximum = arr[i]
            max_index = i
            
    
    if max_index > min_index:
        return max_index + (n - min_index - 2)
    else:
        return max_index + (n - min_index - 1)



arr = [3, 1, 5, 3, 5, 5, 2]
print(arr)
print(find_min_swaps(arr))
# Swap minimum and maximum element in array

# Approach 1: Find the min and max elements in arr by iterating through the arr, and swap them
# Time complexity = O(n)
# Space complexity = O(1)

def swap_min_max_elements(arr):
    min_index = find_min_element_index(arr) # find index of min element
    max_index = find_max_element_index(arr) # find index of max element
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index] # swap them
    return arr


def find_min_element_index(arr):
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def find_max_element_index(arr):
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index 


input = [10, 30, 64, 56]
print(input)
print(swap_min_max_elements(input))

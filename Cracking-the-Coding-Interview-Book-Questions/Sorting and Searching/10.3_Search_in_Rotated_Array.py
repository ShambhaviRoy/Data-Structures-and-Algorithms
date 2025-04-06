# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# Input: Find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)

def search_rotated_array(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] >= arr[low]:
            if arr[low] <= x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_rotated_array(arr, 15))
print(search_rotated_array(arr, 5))

arr = [4,5,6,7,0,1,2]
print(search_rotated_array(arr, 0))
# Binary search
# Given an array, find whether target exists in this array
# Recursive implementation
# Sort the array, compare target with middle element of the array, if target < middle value, check lower part of the array else check upper part
# Base case: when arr has only 1 element --> compare with target
# Time Complexity = O(logn)

def binary_search(arr, target):
    n = len(arr)
    arr.sort()

    if n == 1:
        return arr[0] == target

    if target < arr[n//2]:
        # check in lower half of arr
        binary_search(arr[0: n//2], target)
    elif target > arr[n//2]:
        # check in lower half of arr
        binary_search(arr[n//2: ], target)
    else:
        return True


arr = [1, 3, 5, 2, 7, 10, 33]
target = 5
print(binary_search(arr, target))
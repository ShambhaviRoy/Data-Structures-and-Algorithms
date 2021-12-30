# Linear search: The given data is sequentially scanned to find the target element
# Time complexity = O(n)
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Binary search: The data is assumed to be arranged in ascending order.
# The target element is compared with the middle element. 
# If the target is lesser, the lower part of the array is to be checked, else the upper part has to be checked.
# Time Complexity = O(logn) 
# Iterative approach:
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
    return False

#Recursive approach:
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1 
            return binary_search_recursive(data, target, low, high)
        elif target > data[mid]:
            low = mid + 1
            return binary_search_recursive(data, target, low, high)
    return False

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

print(binary_search_recursive(data, target, 0, len(data)-1))
print(binary_search_iterative(data, target))
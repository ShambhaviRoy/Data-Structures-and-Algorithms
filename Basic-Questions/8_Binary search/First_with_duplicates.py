# Given an array and a key, find index of first occurrence of the key
# Time Complexity = O(n) and Space Complexity = O(1)
def find(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return None

# Approach 2: Using Binary Search
def find_(A, target):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2
        if target < A[mid]:
            high = mid -1
        elif target > A[mid]:
            low = mid + 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print(find(A, 108))
print(find_(A, 108))
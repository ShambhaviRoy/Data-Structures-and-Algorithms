# A fixed point in an array A is such that for index i, A[i] = i

# Naive approach
# Time complexity = O(n) and Space Complexity = O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# Better approaches can be used
# The list is in ascending order and has distinct elements
# Time Complexity = O(logn) and Space complexity = O(1)
def find_fixed_point(A):
    low = 0
    high = len(A)-1
    while low < high:
        mid = (low + high)//2
        if mid < A[mid]:
            high = mid - 1
        elif mid > A[mid]:
            low = mid + 1
        else:
            return A[mid]
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]

print("Linear Approach:")
print(A1)
print(find_fixed_point_linear(A1))
print(A2)
print(find_fixed_point_linear(A2))
print(A3)
print(find_fixed_point_linear(A3))
print("Binary Search Approach:")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))

# Array is bitonically sorted having increasing values, peak and then decreases.
# Find the peak value using binary search

def find_bitonic_peak(A):
    low = 0
    high = len(A) - 1

    # Require atleast 3 elements for a bitonic sequence
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = A[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = A[mid + 1] if mid + 1 < len(A) else float('inf')

        if mid_left < A[mid] and A[mid] < mid_right:
            low = mid + 1
        elif mid_left > A[mid] and A[mid] > mid_right:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
    return None

A = [1, 2, 3, 2, 1]
print(find_bitonic_peak(A))

# Peak element is "5".
A1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A1))
A2 = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A2))
A3 = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A3))
A4 = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A4))



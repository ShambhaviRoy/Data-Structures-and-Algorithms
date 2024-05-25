# Problem: Return index of the smallest number in the cyclically shifted array.
# An array is cyclically shifted if it is possible to shift its entries cyclically so that its sorted.

def find_index_of_smallest(A):
    low = 0
    high = len(A) - 1

    if A[low] < A[high]:
        return low

    minimum = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == A[low] and A[mid] == A[high]:
            low += 1
            high -= 1
            minimum = min(minimum, A[mid])
        elif A[mid] > A[high]:
            low = mid+1
        else:
            minimum = min(minimum, A[mid])
            high = mid-1
    return minimum


A = [7, 1, 2, 3, 4, 5, 6]
idx = find_index_of_smallest(A)
print(A[idx])


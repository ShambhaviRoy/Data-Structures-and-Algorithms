# Problem: Return index of the smallest number in the cyclically shifted array.
# An array is cyclically shifted if it is possible to shift its entries cyclically so that its sorted.

def find_index_of_smallest(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] <= A[high]:
            high = mid
        elif A[mid] > A[high]:
            low = mid - 1

    return low


A = [7, 1, 2, 3, 4, 5, 6]
idx = find_index_of_smallest(A)
print(A[idx])


# Contiguous Sequence: You are given an array of integers (both positive and negative). Find the
# contiguous sequence with the largest sum. Return the sum.
# EXAMPLE
# Input 2, -8, 3, -2, 4, -10
# Output: 5 (i.e., {3, -2, 4})

# arr = [2, -8, 3, -2, 4, -10]
# sums= [] # max subarray sum ending at index i
# sums[i] = sums[i-1] + arr[i] ; if sums[i-1] > 0
#           = arr[i] ; if sums[i] < 0


def contiguous_sequence_sum(arr):
    max_sums = [0] * len(arr)
    max_sums[0] = arr[0]
    for i in range(len(arr)):
        if max_sums[i-1] > 0:
            max_sums[i] = max_sums[i-1] + arr[i]
        else:
            max_sums[i] = arr[i]
    ans = float('-inf')
    for i in range(len(arr)):
        if ans < max_sums[i]:
            ans = max_sums[i]
    return ans

arr = [2, -8, 3, -2, 4, -10]
print(f'Answer = {contiguous_sequence_sum(arr)}')
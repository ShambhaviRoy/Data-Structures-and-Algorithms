# Length of longest subarray with at most k frequency
# Given an integer array nums and an integer k, return the length of the longest subarray with each element having frequency <= k
# Example:
# Input nums = [1, 2, 3, 1, 2, 3, 1, 2], k = 2 --> Output = 6

from collections import Counter

def longest_subarray_atmost_k(nums, k):
    counts = Counter(nums)
    substr_len = 0

    for i in range(len(nums)):
        freq = counts[nums[i]]
        print(f'Element = {nums[i]}, freq = {freq}')
        if freq > k:
            i += 1
            substr_len = 1
        else:
            substr_len += 1

    return substr_len

nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
print(longest_subarray_atmost_k(nums, k))


# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

# https://leetcode.com/problems/arithmetic-slices/

# Approach 1: Use DP
# dp[i] to store the no. of slices till nums[i]
# Time Complexity = O(n), Space Complexity = O(n)

def find_slices(nums):
    ans = 0
    n = len(nums)
    dp = [0]*n

    for i in range(2, n):
        if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
            dp[i] = dp[i-1] + 1
        ans += dp[i]
    return ans



# Approach 2: Space Optimized DP
# Using 2 variables, dp and dpPrev to store number of slices till nums[i]
# Time Complexity = O(n), Space Complexity = O(1)

def find_slices_optimized(nums):
    ans = 0
    dp, dpPrev = 0, 0

    for i in range(2, n):
        if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
            dp = dpPrev + 1
        ans += dp
        dpPrev = dp
        dp = 0
    return ans




if __name__ == '__main__':
    print('Enter number of elements in nums list:')
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    print(find_slices(nums))
    print(find_slices_optimized(nums))



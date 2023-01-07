# https://leetcode.com/problems/sum-of-beauty-in-the-array/description/


# You are given a 0-indexed integer array nums. 
# For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 0, if none of the previous conditions holds.
# Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

# Time Complexity = O(n)
# Space Complexity = O(n)


def sumOfBeauties(nums):
    # iterate through each element in 1 <= i <= len(nums)-2
    # calculate beauty of each, add to ans
    n = len(nums)
    ans = 0

    # maintain minArr to store min value till i
    # maintain maxArr to store max value till i
    minArr = [-1] * n 
    maxArr = [9999] * n
    minArr[0] = nums[0]
    maxArr[-1] = nums[-1]
    for i in range(1, n):
        minArr[i] = max(nums[i-1], minArr[i-1])
    
    for i in range(n-2, -1, -1):
        maxArr[i] = min(nums[i+1], maxArr[i+1]) 

    for i in range(1, len(nums)-1):
        if minArr[i] < nums[i] < maxArr[i]:
            ans += 2
        elif nums[i-1] < nums[i] < nums[i+1]:
            ans += 1

    return ans


nums = [2, 4, 6, 4]
print(sumOfBeauties(nums))
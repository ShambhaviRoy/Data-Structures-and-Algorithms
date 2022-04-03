# Given an array of integers, find the next lexicographically greater permutation

# https://leetcode.com/problems/next-permutation/

# Time Complexity = O(n), Space Complexity = O(1)

# function to reverse the array from start index to end index
# done using 2 pointer - swapping first (start) and last (end) element - doing this till the pointers meet
def reverse(nums, start, end):
    while(start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# given a no., this function finds the next higher number in the right part (after the given no.)
def nextHigher(nums, val, index):
    for i in range(len(nums)-1, index, -1):
        if nums[i] > val:
            return i
    return -1
        

def nextPermutation(nums):
    """
    Modify nums in-place.
    """
    if len(nums) <= 1:
        return nums
    
    for i in (range(len(nums)-1, 0, -1)):
        # find a decreasing element
        if nums[i] > nums[i-1]:
            index = nextHigher(nums, nums[i-1], i-1)
            nums[i-1], nums[index] = nums[index], nums[i-1] #swap
            reverse(nums, i, len(nums)-1)
            return nums
    
    reverse(nums, 0, len(nums)-1)
        
        
print(nextPermutation([1, 2, 3]))
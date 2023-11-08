# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# https://leetcode.com/problems/move-zeroes/


# Approach 1: The question requires 2 conditions, can be satisfied one by one and combined:
# Move all 0's to end
# Maintain relative order of all other elements

# Time Complexity = O(n)
# Space Complexity = O(n)

def move_zeroes_1(nums):
    # count the no. of 0's
    num_zeroes = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            num_zeroes += 1

    ans = []
    # retain order of the non-0 elements
    for i in range(len(nums)):
        if nums[i] != 0:
            ans.append(nums[i])

    # place 0's at the end
    while num_zeroes > 0:
        ans.append(0)
        num_zeroes -= 1

    # Combine
    nums = [ans[i] for i in range(len(nums))]
    return nums


# Approach 2: Maintain 2 pointers, a fast pointer to point to the current element and a slow pointer to point to the last non-zero element. 
# If the current element is non-0, we append it just after the last non-0 element found. Once the non-0 elements are placed, we fill up with 0's

# Time Complexity = O(n)
# Space Complexity = O(1)

def move_zeroes_2(nums):
    last_non_zero_at = 0
    # place non-0 elements
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_at] = nums[i]
            last_non_zero_at += 1
    # fill up with 0's
    for i in range(last_non_zero_at, len(nums)):
        nums[i] = 0
    return nums


# Approach 3: Maintain 2 pointers, a fast pointer to point to the current element and a slow pointer to point to the last non-zero element. 
# All elements before the slow pointer are non-0's, all elements between current and slow pointer are 0's
# When we see a non-0, we swap current and last non-0 and move slow pointer ahead else we just move the current pointer ahead

# Time Complexity = O(n) but best-case time complexity is better than previous approach
# Space Complexity = O(n)

def move_zeroes_3(nums):
    last_non_zero_at = 0
    for cur in range(len(nums)):
        if nums[cur] != 0:
            nums[last_non_zero_at], nums[cur] = nums[cur], nums[last_non_zero_at]
            last_non_zero_at += 1
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes_1(nums))
print(move_zeroes_2(nums))

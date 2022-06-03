# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


# Approach: Greedy
# Sort the given nums array
# Pair the no.s (no.s in pair should be closer to each other to minimize sum)
# Compare and return max pair sum


def find_max_pair_sum(nums):
    nums.sort()

    start = 0
    end = len(nums) - 1
    ans = 0

    while start < end:
       pair_sum = nums[start] + nums[end]
       ans = max(pair_sum, ans)
       start += 1
       end -= 1

    return ans


nums = [3, 5, 2, 2]
print(find_max_pair_sum(nums))

nums1 = [3,5,4,2,4,6]
print(find_max_pair_sum(nums1))

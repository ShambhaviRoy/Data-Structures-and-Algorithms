# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# nums = [0,0,1,1,1,2,2,3,3,4]
# unique elements are at: 0, 2, 5, 7, 9

# Approach: 2 pointers
# Time complexity = O(n)
# Space complexity = O(1)
def removeDuplicates(nums) -> int:
    if not nums:
            return 0

    unique_at = 0

    for element_at in range(1, len(nums)):
        if nums[element_at] != nums[unique_at]:
            unique_at += 1
            nums[unique_at] = nums[element_at]

    return unique_at + 1



nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
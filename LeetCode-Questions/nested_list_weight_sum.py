# 339. Nested List Weight Sum
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
# Return the sum of each integer in nestedList multiplied by its depth.

# https://leetcode.com/problems/nested-list-weight-sum/description/

# Example:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10

def depth_sum(nested_list, depth):
    ans = 0
    for element in nested_list:
        if isinstance(element, int):
            ans += element * depth
        else:
            ans += depth_sum(element, depth + 1)

    return ans

nested_list = [[1,1], 2, [1,1]]
print(depth_sum(nested_list, 1))
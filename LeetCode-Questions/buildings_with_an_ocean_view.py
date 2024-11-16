# 1762. Buildings With an Ocean View
# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

# https://leetcode.com/problems/buildings-with-an-ocean-view/description/

def findBuildings(heights):
    n = len(heights)
    curr_ht = 0
    answer = []
    for i in range(n-1, -1, -1):
        if heights[i] > curr_ht:
            curr_ht = heights[i]
            answer.append(i)
    return answer[::-1]


heights = [4,2,3,1]
print(findBuildings(heights))

heights = [4,3,2,1]
print(findBuildings(heights))

heights = [1,3,2,4]
print(findBuildings(heights))

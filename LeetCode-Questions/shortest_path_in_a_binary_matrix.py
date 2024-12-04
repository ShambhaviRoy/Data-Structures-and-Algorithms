# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Examples:
# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/


# Approach: BFS from (0, 0) to (n - 1, n - 1) stepping only on cells == 0, keep track of the length of path

from collections import deque

directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def is_valid_coordinate(x, y, n, visited):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1 and (x, y) not in visited


def shortest_path(grid):
    n = len(grid)

    source = (0, 0)
    destination = (n - 1, n - 1)

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1 

    queue = deque()
    queue.append((source, 1))
    visited = set()
    visited.add(source)

    while queue:
        node, path = queue.popleft()
        x, y = node
        if node == destination:
            return path
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if is_valid_coordinate(new_x, new_y, n, visited) and grid[new_x][new_y] == 0:
                queue.append(((new_x, new_y), path + 1))
                visited.add((new_x, new_y))

    return -1
            

grid1 = [[0,1],[1,0]]
print(shortest_path(grid1) == 2)

grid2 = [[0,0,0],[1,1,0],[1,1,0]]
print(shortest_path(grid2) == 4)

grid3 = [[1,0,0],[1,1,0],[1,1,0]]
print(shortest_path(grid3) == -1)
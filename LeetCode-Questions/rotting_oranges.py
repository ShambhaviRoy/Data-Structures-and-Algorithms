# Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Approach:
# Multi-source BFS (from each rotten orange) per minute, and increment minutes (ans)
# Time Complexity = O(m + n), Space Complexity = O(m + n)

from collections import deque

def is_valid_coordinate(i, j, m, n):
    return 0 <= i < m and 0 <= j < n

def orangesRotting(grid):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m, n  = len(grid), len(grid[0])

    fresh = 0
    rotten = deque()
    ans = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh += 1
            if grid[i][j] == 2:
                rotten.append((i, j))

    while fresh > 0 and rotten:
        ans += 1
        for _ in range(len(rotten)): # multi-source BFS
            current_rotten = rotten.popleft()
            i, j = current_rotten
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                if is_valid_coordinate(new_i, new_j, m, n) and grid[new_i][new_j] == 1:
                    fresh -= 1
                    grid[new_i][new_j] = 2
                    rotten.append((new_i, new_j))
        

    return ans if fresh == 0 else -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))


grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))

    

    
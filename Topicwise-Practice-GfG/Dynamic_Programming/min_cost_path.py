# Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). 
# Each cell of the matrix represents a cost to traverse through that cell. 
# The total cost of a path to reach (m, n) is the sum of all the costs on that path (including both source and destination). 
# You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed. 
# You may assume that all costs are positive integers.

import sys


# Approach: Recursive Implementation
def find_min_cost(cost, start, end):
    if start < 0 or end < 0:
        return sys.maxsize
    
    elif start == 0 and end == 0:
        return cost[start][end]

    else:
        return cost[start][end] + min(find_min_cost(cost, start-1, end), 
                                        find_min_cost(cost, start, end-1), 
                                        find_min_cost(cost, start-1, end-1))

    

# Approach: Dynamic Programming 
# Storing the cost in a dp matrix
def find_min_cost_iterative(cost, start, end):
    dp = [[0] * len(cost[0])]* (len(cost))

    dp[0][0] = cost[0][0]
    
    # initializing the first column of dp matrix
    for i in range(1, start+1):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    # initializing the first row of dp matrix 
    for j in range(1, end+1):
        dp[0][j] = dp[0][j-1] + cost[0][j]

    for i in range(1, start+1):
        for j in range(1, end+1):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 

    return dp[start][end]

    




cost= [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

print(find_min_cost(cost, 2, 2))

print(find_min_cost_iterative(cost, 2, 2))
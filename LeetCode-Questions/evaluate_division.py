# Calculate value of equation
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
class Solution:
    def calcEquation_BFS(self, equations, values, queries):
#         solution using BFS
        G = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v
            
        def bfs(source, dest):
            if not (source in G and dest in G):
                return -1.0
            queue = [(source, 1.0)]
            seen = set()
            while len(queue) > 0:
                node, val = queue.pop()
                if node == dest:
                    return val
                seen.add(node)
                for y in G[node]:
                    if y not in seen:
                        queue.append((y, val*G[node][y]))
            return -1.0
 
        return [bfs(s, d) for s, d in queries]
                

s = Solution()
print(s.calcEquation_BFS([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
))
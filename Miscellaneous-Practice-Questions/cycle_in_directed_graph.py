# Code to detect cycle in directed graph

# Approach: 
# Use DFS, check if a vertex is already visited --> cycle
# Stop when we find a cycle

# Time Complexity = O(V+E)
# Space Complexity = (V)

from collections import defaultdict

class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclic_helper(self, node, visited, stack):
        visited[node] = True
        stack[node] = True
        for neighbor in self.graph[node]:
            if visited[neighbor] == False:
                if self.isCyclic_helper(neighbor, visited, stack) == True:
                    return True
            elif stack[neighbor] == True:
                return True
        stack[node] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        stack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclic_helper(node, visited, stack) == True:
                    return True
        return False



g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic():
    print('Yes')
else:
    print('No')
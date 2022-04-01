# Given a directed acyclic graph, print its topological sort

from collections import defaultdict
from pydoc import Helper

class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list) # edges
        self.V = vertices   # no. of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topological_sort_helper(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_helper(i, visited, stack)
            stack.append(v)


    def topological_sort(self):
        visited = [False] * (self.V + 1)
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_helper(i, visited, stack)
        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topological_sort()
 
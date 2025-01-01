# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

# Approach: Using BFS (iterative, with a queue)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def BFS(self, start, end):
        queue = []
        visited = []
        queue.append(start)
        visited.append(start)

        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if i == end:
                    return True
                else:
                    visited.append(i)
                    queue.append(i)

        return False


graph = Graph()
graph.addEdge('a', 'b')
graph.addEdge('a', 'c')
graph.addEdge('b', 'a')
graph.addEdge('b', 'd')
graph.addEdge('c', 'a')
graph.addEdge('c', 'd')
graph.addEdge('d', 'e')
graph.addEdge('e', 'd')
graph.addEdge('d', 'f')
graph.addEdge('f', 'g')


print(graph.BFS('a', 'd'))
print(graph.BFS('a', 'e'))
print(graph.BFS('g', 'd'))

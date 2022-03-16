# Breadth First Search

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = []
        queue = []
        queue.append(s)
        visited.append(s)

        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

# graph_elements = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["e"],
#    "e" : ["d"]
# }

graph = Graph()
graph.addEdge('a', 'b')
graph.addEdge('a', 'c')
graph.addEdge('b', 'a')
graph.addEdge('b', 'd')
graph.addEdge('c', 'a')
graph.addEdge('c', 'd')
graph.addEdge('d', 'e')
graph.addEdge('e', 'd')


graph.BFS('a')

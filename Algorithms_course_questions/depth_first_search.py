# Depth First Search

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFS_help(self, v, visited):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.DFS_help(i, visited)

    def DFS(self, v):
        visited = set()
        self.DFS_help(v, visited)

    

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


graph.DFS('a')

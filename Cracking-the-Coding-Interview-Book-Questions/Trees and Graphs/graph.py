class Graph:
    def __init__(self):
        self.graph = []

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_undirected_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def add_directed_edge(self, start, end):
        if start in self.graph:
            self.graph[start].append(end)
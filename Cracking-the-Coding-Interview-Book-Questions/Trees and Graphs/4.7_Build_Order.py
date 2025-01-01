# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

from collections import deque

class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.dependencies = 0 # in-degree of node

    def add_neighbor(self, end):
        self.neighbors.append(end)
        end.increment_dependencies()
    
    def increment_dependencies(self):
        self.dependencies += 1

    def decrement_dependencies(self):
        self.dependencies -= 1


class Graph:
    def __init__(self):
        self.nodes = set()
        self.map = {} # name of node : node object

    def get_or_create_node(self, name):
        if name not in self.map:
            node = Node(name, [])
            self.map[name] = node
            self.nodes.add(node)
        return self.map[name]
    
    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)

    def print_graph(self):
        for node in self.nodes:
            print(f'Node = {node.name}, Neighbors = {[x.name for x in node.neighbors]}, Dependencies = {node.dependencies}')
    



def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)

    for dependency in dependencies:
        start, end = dependency
        graph.add_edge(start, end)

    return graph
    

def order_projects(graph):
    order = []
    order, end_of_list = add_non_dependents(order, graph, 0)
    
    to_be_processed = 0
    while to_be_processed < len(graph):
        current = order[to_be_processed]
        if not current:
            return None
        children = current.neighbors
        for child in children:
            child.decrement_dependencies()
        order, end_of_list = add_non_dependents(order, children, end_of_list)
        to_be_processed += 1

    return order
        

def add_non_dependents(order, projects, index):
    for project in projects:
        if project.dependencies == 0:
            order.append(project)
            index += 1
    return order, index


def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    print('Input graph:')
    graph.print_graph()
    print('---')
    build_order = order_projects(graph.nodes)
    return build_order


if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    ans = find_build_order(projects, dependencies)
    print(f'Final build order = {[x.name for x in ans]}')


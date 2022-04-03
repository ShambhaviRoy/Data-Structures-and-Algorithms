from collections import defaultdict

class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.count = size

    # The find function - optimized with 'path compression'
    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    # The union function - optimized with 'union by rank'
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
        self.count -= 1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:    
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        n = len(pairs)
        uf = UnionFind(n)
        
        # iterate over edges to connect them
        for pair in pairs:
            node1, node2 = pair
            uf.union(node1, node2)
            
        # dict to store root and vertices (indices) having that root
        root_to_component = defaultdict(list)
        for vertex in range(len(s)):
            root = uf.find(i)
            root_to_component[root].append(vertex)
            
        # iterate over each connected component
        smallest_string = ''
        for root, vertices in root_to_component.items():
            characters = []
            for i in vertices:
                characters.append(s[i])
            characters.sort()
            for i in vertices:
                smallest_string.append(characters[i])
                
        return smallest_string
            
        
s = Solution()
print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))

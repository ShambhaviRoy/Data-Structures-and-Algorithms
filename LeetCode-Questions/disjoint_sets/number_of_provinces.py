# Number of provinces

# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3846/

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

    def get_count(self):
        return self.count



class Solution:
    def findCircNum(self, isConnected):
        if not isConnected or len(isConnected) == 0:
            return 0

        n = len(isConnected)
        uf = UnionFind(n)

        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)

        return uf.get_count()


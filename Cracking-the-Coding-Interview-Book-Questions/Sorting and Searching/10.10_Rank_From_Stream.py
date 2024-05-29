# Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
# to be able to look up the rank of a number x (the number of values less than or equal to x).
# Implement the data structures and algorithms to support these operations. That is, implement
# the method track(int x), which is called when each number is generated, and the method
# getRankOfNumber(int x), which returns the number of values less than or equal to x (not
# including x itself).
# EXAMPLE
# Stream (in order of appearance): [5, 1, 4, 4, 5, 9, 7, 13, 3]
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3


class RankNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.rank = 0
        self.left_size = 0


    def insert(self, d):
        if d <= self.data:
            if not self.left:
                self.left = RankNode(d)
            else:
                self.left.insert(d)
            self.left_size += 1
        else:
            if not self.right:
                self.right = RankNode(d)
            else:
                self.right.insert(d)


    def get_rank(self, x):
        if x == self.data:
            return self.left_size
        elif x < self.data:
            if not self.left:
                return -1
            return self.left.get_rank(x)
        else:
            if not self.right:
                right_rank = -1
            else:
                right_rank = self.right.get_rank(x)
            return self.left_size + 1 + right_rank


class RankNodeBST:
    def __init__(self):
        self.root = None

    def track(self, number):
        if not self.root:
            self.root = RankNode(number)
        else:
            self.root.insert(number)
    
    def get_rank(self, number):
        return self.root.get_rank(number)


tree = RankNodeBST()
stream = [5, 1, 4 , 4, 5, 9, 7, 13, 3]

for number in stream:
    tree.track(number)

# get rank methods
print(tree.get_rank(1))
print(tree.get_rank(3))
print(tree.get_rank(4))

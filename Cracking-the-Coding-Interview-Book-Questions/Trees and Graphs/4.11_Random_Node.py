# Random Node: You are implementing a binary search tree class from scratch, which, in addition
# to insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for get RandomNode, and explain how you would implement the rest of the methods.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 0


    def get_random_node(self):
        # probability of getting a node = 1/n
        if self.left:
            left_size = self.left.size
        else:
            left_size = 0
        random = random.randint()
        if random < left_size:
            return self.left.get_random_node()
        elif random == left_size:
            return self
        else:
            return self.right.get_random_node()
        

    def insert_in_order(self, d):
        if d <= self.value:
            if not self.left:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if not self.right:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1

    
    def find(self, d):
        if self.value == d:
            return self
        elif d <= self.value:
            if not self.left:
                return None
            else:
                return self.left.find(d)
        elif d > self.value:
            if not self.right:
                return None
            else:
                return self.right.find(d)




# Given the root node of a binary search tree and 2 integers low and high, returh the sum of values of all nodes with a value in hte inclusive range [low, high]

# BST implementation

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print('Value already in the tree!')


def range_sum(root, low, high):
    if not root:
        return 0

    ans = 0

    if root.value in range(low, high + 1):
        ans += root.value

    ans += range_sum(root.left, low, high)
    ans += range_sum(root.right, low, high)
    
    return ans




bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(18)

print(range_sum(bst.root, 7, 15))




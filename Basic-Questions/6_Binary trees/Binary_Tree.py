class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
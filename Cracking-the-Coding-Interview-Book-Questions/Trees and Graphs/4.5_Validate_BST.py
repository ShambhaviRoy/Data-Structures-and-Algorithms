# Implement a function to check if a binary tree is a binary search tree.


import sys
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def check_BST(self, root):
        return self.check_BST_helper(root, -sys.maxsize+1, sys.maxsize)
    
    def check_BST_helper(self, node, min, max):
        if not node:
            return True
        if node.value <= min or node.value > max:
            return False
        return self.check_BST_helper(node.left, min, node.value) and self.check_BST_helper(node.right, node.value, max)

    



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.left = TreeNode(7)
tree.left.left.left.left = TreeNode(8)

print(tree.check_BST(tree))
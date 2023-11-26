# Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

import sys
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def check_height(self, root):
        if not root:
            return -1
        left_height = self.check_height(root.left)
        if left_height == sys.maxsize:
            return sys.maxsize
        right_height = self.check_height(root.right)
        if right_height == sys.maxsize:
            return sys.maxsize
        height_diff = right_height - left_height
        if(abs(height_diff) > 1):
            return sys.maxsize
        else:
            return max(left_height, right_height) + 1


    def is_balanced(self, root):
        return self.check_height(root) != sys.maxsize
    



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.left = TreeNode(7)
tree.left.left.left.left = TreeNode(8)

print(tree.is_balanced(tree))
# Implement a function to check if a binary tree is a binary search tree.


import sys
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach: Use the property left.data <= node.data < right.data
# check whether the node value is in the range [min, max], min and max depend on the node
# Time Complexity = O(N), Space Complexity = O(log N), N = no.of nodes in tree

def check_BST(root):
    return check_BST_helper(root, -sys.maxsize+1, sys.maxsize)

def check_BST_helper(node, min, max):
    if not node:
        return True
    if node.value <= min or node.value > max:
        return False
    return check_BST_helper(node.left, min, node.value) and check_BST_helper(node.right, node.value, max)

    



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.left = TreeNode(7)
tree.left.left.left.left = TreeNode(8)

print(check_BST(tree))

tree = TreeNode(20)
tree.left = TreeNode(10)
tree.right = TreeNode(30)
tree.right.left = TreeNode(25)
print(check_BST(tree))
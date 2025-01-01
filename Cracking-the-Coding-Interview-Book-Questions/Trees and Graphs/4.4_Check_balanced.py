# Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

import sys
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time Complexity = O(N), Space Complexity = O(H), N = no. of nodes, H = height of tree
def check_height(root):
    if not root:
        return -1
    left_height = check_height(root.left)
    if left_height == sys.maxsize:
        return sys.maxsize
    right_height = check_height(root.right)
    if right_height == sys.maxsize:
        return sys.maxsize
    height_diff = right_height - left_height
    if(abs(height_diff) > 1):
        return sys.maxsize
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height(root) != sys.maxsize
    



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.left = TreeNode(7)
tree.left.left.left.left = TreeNode(8)

print(is_balanced(tree))


# Not optimal as it calls check_node_height() repeatedly on each node --> Time complexity = O(N log N)
def check_node_height(node):
    if not node:
        return -1
    return max(check_node_height(node.left), check_node_height(node.right)) + 1

def is_tree_balanced(node):
    if not node:
        return True
    left_ht = check_node_height(node.left)
    right_ht = check_node_height(node.right)
    diff = left_ht - right_ht
    return abs(diff) <= 1


# unbalanced tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.left.left.left = TreeNode(7)
tree.left.left.left.left = TreeNode(8)

print(is_tree_balanced(tree))

# balanced tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
print(is_tree_balanced(tree))
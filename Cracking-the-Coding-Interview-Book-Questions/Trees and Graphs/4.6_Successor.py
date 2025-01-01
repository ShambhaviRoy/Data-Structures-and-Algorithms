# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.

# In order traversal: left -> node -> right

# def in_order_successor(Node n):
#     if n has a right subtree:
#         return leftmost child of right subtree
#     else:
#         while n is a right child of n.parent:
#             n = n.parent --> go up
#         return n.parent --> parent has not been traversed

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def left_most_child(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def in_order_successor(node):
    if not node: 
        return None
    if node.right:
        # finding leftmost child of the right subtree
        return left_most_child(node.right)
    else:
        n = node
        n_parent = node.parent
        # go up
        while(n_parent and n_parent.left != n):
            n_parent = n.parent
            n = n.parent
        return n.parent



tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.parent = tree

node = TreeNode(1)
tree.left.left = node
tree.left.left.parent = tree.left

tree.left.right = TreeNode(3)
tree.left.right.parent = tree.left

tree.right = TreeNode(6)
tree.right.parent = tree

tree.right.left = TreeNode(5)
tree.right.left.parent = tree.right

print(in_order_successor(node).value)
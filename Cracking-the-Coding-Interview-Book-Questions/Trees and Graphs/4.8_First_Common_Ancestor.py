# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

class TreeNode:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None


# to check whether the node is covered in tree with root
def covers(root, p):
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


#method to get sibling of node
def get_sibling(node):
    if not node or not node.parent:
        return None
    parent = node.parent
    if parent.left == node:
        return parent.right
    else:
        return parent.left
    
# Time Complexity = O(t), t = size of subtree of the first common ancestor, can be n (= no. of nodes) in worst case
def commmon_ancestor(root, p, q):
    if(not covers(root, p) or not covers(root, q)):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q
    # travel upwards from p until a node covering q is found
    sibling = get_sibling(p)
    parent = p.parent
    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent
    

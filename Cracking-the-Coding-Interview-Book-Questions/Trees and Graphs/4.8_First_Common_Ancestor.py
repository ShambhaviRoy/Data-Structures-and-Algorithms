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


# Approach 1: With link to parent
# Find the depth of each node
# Traverse from the deeper node up the parent until it reaches the level of shallow node
# Traverse from both until we reach a common node --> first ancestor
# Time Complexity = O(d), d = depth of tree
# Space Complexity = O(1)
def find_first_common_ancestor(node1, node2):
    depth1 = get_depth(node1)
    depth2 = get_depth(node2)
    deep = node1 if depth1 > depth2 else node2
    shallow = node2 if depth1 > depth2 else node1
    # go up from deep
    deep = go_up(deep, abs(depth1 - depth2))
    # traverse up from both until they're equal
    while deep != shallow and deep and shallow:
        deep = deep.parent
        shallow = shallow.parent
    if not deep or not shallow:
        return None
    return deep

def go_up(node, levels):
    while levels > 0:
        node = node.parent
        levels -= 1
    return node


def get_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.parent
    return depth

# Approach 2: Traverse path from one node to check if its subtree covers the other node
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
    

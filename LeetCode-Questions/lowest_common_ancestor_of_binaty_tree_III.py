# 1650. Lowest Common Ancestor of a Binary Tree III
# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/


# path_p = path from node p to root, path_q = path from node q to root
# path_p = [p, a, b, root]
# path_q = [q, x, b, root], ans = b (traverse path_p and path_q until we find the common node --> LCA)

#    root
#   y   b
# z     a   x
#      p    q

class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_path_to_root(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    path_p = get_path_to_root(p)
    path_q = get_path_to_root(q)
    i = len(path_p) - 1
    j = len(path_q) - 1

    while path_p[i] == path_q[j]:
        i += 1
        j += 1

        
    return root


def create_binary_tree(arr, tree):
    return None


def inorder_traversal(root):
    # left --> root --> right
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


arr = [3,5,1,6,2,0,8, None, None,7,4]
tree = create_binary_tree(arr, None)
inorder_traversal(tree)
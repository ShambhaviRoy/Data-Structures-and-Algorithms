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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def depth_of_node(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

def lowestCommonAncestor(p: Node, q: Node) -> Node:
    p_depth = depth_of_node(p)
    q_depth = depth_of_node(q)

    if p_depth > q_depth:
        deep, shallow = p, q
        deep_depth, shallow_depth = p_depth, q_depth
    else:
        deep, shallow = q, p
        deep_depth, shallow_depth = q_depth, p_depth

    while deep_depth > shallow_depth:
        deep = deep.parent
        deep_depth -= 1

    # now deep_depth == shallow_depth
    while deep != shallow:
        deep = deep.parent
        shallow = shallow.parent

    return deep

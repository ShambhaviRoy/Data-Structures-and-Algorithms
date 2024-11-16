# 314. Binary Tree Vertical Order Traversal
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

# For a node at (x, y), it's left child is at (x + 1, y - 1) and right child is at (x + 1, y - 1)
# x = horizontal level and y = vertical level

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root):
    if not root:
        return []
    
    # BFS
    queue = deque()
    vertical_levels = defaultdict(list)
    queue.append((root, (0, 0)))
    vertical_levels[0].append(root)

    while len(queue) > 0:
        node, coordinate = queue.popleft()
        x, y = coordinate
        if node.left:
            queue.append((node.left, (x + 1, y - 1)))
            vertical_levels[y - 1].append(node.left)
        if node.right:
            queue.append((node.right, (x + 1, y + 1)))
            vertical_levels[y + 1].append(node.right)

    answer = []
    for level in sorted(vertical_levels.keys()):
        print(f'level:{level}, node values:{[x.val for x in vertical_levels[level]]}')
        answer.append(vertical_levels[level])

    return answer



# create binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)

levels =  verticalOrder(root)

for level in levels:
    print([x.val for x in level])
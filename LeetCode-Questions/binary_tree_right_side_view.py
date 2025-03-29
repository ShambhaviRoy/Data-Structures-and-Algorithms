# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# https://leetcode.com/problems/binary-tree-right-side-view/description/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: BFS (level traversal)
# The node in the right side view would be the last node at each level
def right_side_view_BFS(root):
    ans = []
    queue = deque()
    queue.append(root)
    while queue:
        ans.append(queue[-1].val)
        next_level = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
    return ans


# Approach 2: Slightly different BFS
def right_side_view_BFS2(root):
    ans = []
    queue = deque()
    queue.append(root)
    while queue:
        val = None
        for _ in range(len(queue)):
            node = queue.popleft()
            val = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(val)
    return ans



# Approach 3: DFS
def right_view(root, ans, depth):
    if not root:
        return
    if len(ans) == depth:
        ans.append(root.val)
    depth += 1
    right_view(root.right, ans, depth)
    right_view(root.left, ans, depth)
    
    
def right_view_DFS(root):
    ans = []
    right_view(root, ans, 0)  
    return ans     





tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(4)

print(right_side_view_BFS(tree))
print(right_side_view_BFS2(tree))
print(right_view_DFS(tree))
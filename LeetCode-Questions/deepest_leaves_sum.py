# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Approach: BFS, add values of nodes at each level


class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


    def deepest_leaves_sum(self, root):
        queue = [root]
        ans = 0

        while queue:
            ans = 0
            for _ in range(len(queue)):
                node = queue.pop[0]
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                

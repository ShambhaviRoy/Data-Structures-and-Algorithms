# Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path_with_sum(root, target):
    return paths_with_sum(root, 0, target)

def paths_with_sum(root, sum_so_far, target):
    if not root:
        return False
    sum_so_far += root.value
    if sum_so_far == target:
        return True
    else:
        return paths_with_sum(root.left, sum_so_far, target) or paths_with_sum(root.right, sum_so_far, target)



def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end = ' ')
        inorder_traversal(root.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(7)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

inorder_traversal(root)
print('\n')

print(has_path_with_sum(root, 0))
print(has_path_with_sum(root, 12))
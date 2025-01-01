# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
def create_minimal_BST(arr):
    return create_minimal_BST2(arr, 0, len(arr)-1)


def create_minimal_BST2(arr, start, end):
    if end <= start:
        return 
    mid = (start + end)//2
    n = TreeNode(arr[mid])
    n.left = create_minimal_BST2(arr, start, mid-1)
    n.right = create_minimal_BST2(arr, mid+1, end)
    return n
    

def tree_from_arr(arr):
    if len(arr) == 0:
        return 
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = tree_from_arr(arr[0 : mid])
    root.right = tree_from_arr(arr[mid + 1 : ])
    return root


def print_tree(tree):
    root = tree
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Print the current level
        print(" ".join(map(str, level)))


arr = [4, 7, 50, 55, 87, 90]
treeNode = create_minimal_BST(arr)
print_tree(treeNode)
print('---')
tree = tree_from_arr(arr)
print_tree(tree)
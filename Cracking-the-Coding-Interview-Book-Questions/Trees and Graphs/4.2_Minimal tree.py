# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def create_minimal_BST(self, arr):
        return self.create_minimal_BST2(arr, 0, len(arr)-1)

    
    def create_minimal_BST2(self, arr, start, end):
        if end <= start:
            return None
        mid = (start + end)//2
        n = TreeNode(arr[mid])
        n.left = self.create_minimal_BST2(arr, start, mid-1)
        n.right = self.create_minimal_BST2(arr, mid+1, end)
        return n




arr = [4, 7, 50, 55, 87, 90]
treeNode = TreeNode(0)
treeNode.create_minimal_BST(arr)







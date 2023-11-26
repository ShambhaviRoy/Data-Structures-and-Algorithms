# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you 'll have D linked lists).


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def list_of_depths(self, root):
        if not root:
            return None
        
        queue = [root]
        result = []

        while queue:
            ll = LinkedList()
            for _ in range(len(queue)):
                node = queue.pop(0)
                ll.next = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                result.append(ll)

        return result



class LinkedList:
    def __init__(self):
        self.val = 0
        self.next = None



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)

print(tree.list_of_depths(tree))
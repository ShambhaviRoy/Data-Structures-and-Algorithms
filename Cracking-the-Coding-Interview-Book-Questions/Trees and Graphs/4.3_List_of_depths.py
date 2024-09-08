# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you 'll have D linked lists).

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # list of depths using BFS
    def list_of_depths_BFS(self, root):
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        
        result = []

        while queue:
            ll = LinkedListNode('*')
            dummy = ll
            for _ in range(len(queue)):
                node = queue.popleft()
                dummy.next = LinkedListNode(node.val)
                dummy = dummy.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(ll.next)

        return result



class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(self):
    head = self
    while head:
        print(head.val)
        head = head.next


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)

level_lists = tree.list_of_depths_BFS(tree)
for i in range(len(level_lists)):
    print('Level:', i)
    print_list(level_lists[i])
    print('--------')
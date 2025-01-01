# Random Node: You are implementing a binary search tree class from scratch, which, in addition
# to insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for get RandomNode, and explain how you would implement the rest of the methods.

import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1   # no. of left and right nodes


    # Approach 1: Generate a random no. to locate node

    def random_integer(self):
        return random.randint(0, self.size)

    def get_random_node(self):
        # probability of getting a node = 1/n
        if self.left:
            left_size = self.left.size
        else:
            left_size = 0
        r = self.random_integer()
        if r < left_size:
            return self.left.get_random_node()
        elif r == left_size:
            return self
        else:
            if self.right:
                return self.right.get_random_node()


    # Approach 2: Generate a random no. to locate the node
    # Subtract LEFT_SIZE + 1 if we go right
    def get_random_node2(self):
        i = self.random_integer()
        return self.get_ith_node(i)


    def get_ith_node(self, i):
        if self.left:
            left_size = self.left.size
        else:
            left_size = 0
        if i < left_size:
            return self.left.get_ith_node(i)
        elif left_size == i:
            return self
        else:
            if self.right:
                return self.right.get_ith_node(i - (left_size + 1))
        

    def insert_in_order(self, d):
        if d <= self.value:
            if not self.left:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if not self.right:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1

    
    def find(self, d):
        if self.value == d:
            return self
        elif d <= self.value:
            if not self.left:
                return None
            else:
                return self.left.find(d)
        elif d > self.value:
            if not self.right:
                return None
            else:
                return self.right.find(d)


    def delete(self, d):
        # returns new root of tree
        if not self:
            return self
        if d < self.value:
            return self.delete(self.left, d)
        elif d > self.value:
            return self.delete(self.right, d)
        else:
            # found node to be deleted
            # 1. Node has no children
            if not self.left and not self.right:
                return None
            # 2. Node has 1 child
            if not self.left: 
                return self.right
            if not self.right:
                return self.left
            # 3. Node has 2 children- replace the node with its in-order successor (smallest value in right subtree)
            successor = self.right.find_min()
            self.value = successor.value
            self.right = self.right.delete(successor.value)
        return self


    def find_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end = ' ')
        inorder_traversal(root.right)

def print_node(node):
    if not node:
        print('None node found')
    else:
        if node.left and node.right:
            print(f'Found = {node.value}, Left child = {node.left.value}, Right child = {node.right.value}')
        elif node.left and not node.right:
            print(f'Found = {node.value}, Left child = {node.left.value}, Right child = None')
        elif not node.left and node.right:
            print(f'Found = {node.value}, Left child = None, Right child = {node.right.value}')
    


root = TreeNode(5)
print('Input:')
inorder_traversal(root)
print('\n')


arr = [2, 3, -1, 4, 6, 7, -8, 10, 20]
for i in arr:
    root.insert_in_order(i)


root.insert_in_order(-16)
root.insert_in_order(0)
root.insert_in_order(12)
print('Post insertion:')
inorder_traversal(root)
print('\n')

print('Found nodes:')
print_node(root.find(-8))
print_node(root.find(9))
print('\n')

print('Get random nodes:')
print_node(root.get_random_node())
print_node(root.get_random_node2())
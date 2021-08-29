# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        #if linked list is empty
        if self.head is None:
            self.head = new_node
            return
        #if linked list is not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def partition(self, x):
        cur = self.head
        # LLs to store two parts
        left = LinkedList()
        right = LinkedList()
        # Appending nodes to left and right LL
        while cur:
            if cur.data < x:
                left.append(cur.data)
            elif cur.data >= x:
                right.append(cur.data) 
        # Merging both left and right
        while left.node:
            if left.node.next == None: # last node of left LL found
                left.node.next = right.head
        return left


llist = LinkedList()
llist.append(3)
llist.append(5)
llist.append(8)
llist.append(5)
llist.append(10)
llist.append(2)
llist.append(1)
l1 = llist.partition(5)
l1.print_list()

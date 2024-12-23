# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            # get last node
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.next = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def delete_middle_node(self, target):
        if (target == None) or (target.next == None):
            return False
        nxt = target.next
        target.data = nxt.data
        target.next = nxt.next
        return True

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
print("Original Linked List:")
llist.print_list()
llist.delete_middle_node(llist.head.next)
print("Edited Linked List:")
llist.print_list()

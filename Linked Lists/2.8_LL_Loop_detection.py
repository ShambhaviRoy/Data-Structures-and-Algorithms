# Loop detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier)
# Output: C

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):     #insert element at the end of linked list
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

    def find_beg(self):
        slow = self.head
        fast = self.head
        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if (fast == None) and (fast.next == None):
            return None
        slow = head
        while (slow != fast):
            slow = slow.next
            fast = fast.next
        return fast

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("B")
llist.append("D")
print("Original LL:")
llist.print_list()
ans = llist.find_beg()
print(ans) 
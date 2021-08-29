# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node = new_node

    # k= 2 means second last element
    def k_to_last(self, k):
        node1 = self.head
        node2 = self.head
        count = 0
        if self.head is None:
            return None
        while node1:
            count += 1
            if count >= k:
                break
            node1 = node1.next
        while node1 and node2.next:
            node1 = node1.next
            node2 = node2.next
        return node2.data

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
print(llist.k_to_last(2))





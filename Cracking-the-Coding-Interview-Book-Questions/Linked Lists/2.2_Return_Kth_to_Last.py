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
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


    # k= 2 means second last element
    def k_to_last(self, k):
        node1 = self.head
        node2 = self.head
        count = 0
        if self.head is None:
            return None
        for i in range(k):
            node1 = node1.next
        print(f'node1.data = {node1.data}, node2.data = {node2.data}')
        
        while node1 and node2:
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
llist.print_list()
print(f'kth to last node: {llist.k_to_last(2)}')





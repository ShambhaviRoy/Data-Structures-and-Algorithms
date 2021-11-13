class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head 
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                #new node is to be added after the last node- append
                self.append(data)
                return
            elif cur.data == key:
                #new node is to be added after node other than last
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                #insert before head node- prepend
                self.prepend(data)
            elif cur.data == key:
                #new node is to be added before node other than head
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                new_node.next = cur
                cur.prev = new_node
                new_node.prev = prev
                return
            cur = cur.next

dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(3,6)
dllist.add_before_node(4,9)

dllist.print_list()







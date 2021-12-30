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

    def pairs_with_sum(self, sum_val):
        pairs = list()
        cur = self.head 
        nxt = None 
        while cur:
            nxt = cur.next
            while nxt:
                if cur.data + nxt.data == sum_val:
                    pairs.append("(" + str(cur.data) + "," + str(nxt.data) + ")")
            nxt = nxt.next
        cur = cur.next
        return pairs


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))
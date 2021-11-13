class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #if the circular linked list is empty
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        #if the circular linked list is not empty
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break 

    #Add a node to the starting of the circular linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove_node(self, key):
        #Assume that each node is unique. We have to remove the node whose key is given
        if self.head:
            if self.head.data == key:
                #if the key of head node is given to be removed
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                #To remove another node
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next
    
cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()           

cllist.remove_node("A")
cllist.remove_node("C")
cllist.print_list()

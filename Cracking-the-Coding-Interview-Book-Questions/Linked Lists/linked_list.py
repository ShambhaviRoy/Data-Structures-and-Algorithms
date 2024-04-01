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
            
    def lengthList(self):
        cur = self.head 
        length = 0
        while cur:
            length += 1
            cur = cur.next 
        return length
    
    def getLastNode(self):
        last = self.head
        nxt = last.next
        while nxt != None:
            last = nxt 
            nxt = last.next
        return last
    

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if(pos == 0):
            new_node.next = self.head
            self.head.next = new_node
        prev = self.head
        for i in range(pos):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        return self.head

    
    def delete_at_position(self, pos):
        if(pos == 0):
            self.head = self.head.next
        prev = None
        prev.next = self.head
        for i in range(pos):
            prev = prev.next
        prev.next = prev.next.next
        return self.head
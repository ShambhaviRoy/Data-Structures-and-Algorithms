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

    def remove_duplicates(self):
        cur = self.head
        seen = dict()        #A dict to store DLL data and number of occurrences 
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
        
    def delete_node(self, node):
        #For deletion process, the entire node is compared instead of using only key
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                #Case 1- Only 1 node in DLL(head) to be deleted
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                
                #Case 2- Delete head node from DLL
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                #Case 3- Delete other than head node when cur.next is not None
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                else:
                    #Case 4- Delete node other than head when cur.next is None (last node)
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)
print("Given DLL:")
dllist.print_list()

dllist.remove_duplicates()
print("DLL with duplicates removed:")
dllist.print_list()
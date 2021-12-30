class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL():
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

#To calculate length of circular linked list
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
            if cur.next == self.head:
                break
        return count

    def remove_node(self, node):
        if self.head:
            if self.head == node:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next 
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next 
                    if cur == node:
                        prev.next = cur.next
                        cur = cur.next


    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1 :
            count = 1
            while count != step:
                cur = cur.next
                count += 1 
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

cllist = CircularLL()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

cllist.josephus_circle(2)
cllist.print_list()

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

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLL()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()


# A -> B -> C -> D -> ...
# A -> B -> ... and C -> D -> ...

cllist = CircularLL()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

cllist.split_list()
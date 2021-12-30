#WAP to find if a given list is Circular Linked List or not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_LL:
    def __init__(self):
        self.head =  None

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

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

cllist = Circular_LL()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

input_list = Circular_LL()
input_list.append(1)
input_list.append(2)
input_list.append(3)
input_list.append(4)

print(cllist.is_circular_linked_list(input_list))



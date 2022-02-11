# Rotate a linked list k times to the right (k < length of the list)
# Example: 
# Input: 1 --> 2 --> 3 --> 4 --> 5 --> None, k = 2
# 5--> 1 --> 2 --> 3 --> 4 --> None (after 1 rotation)
# 4 --> 5 --> 1 --> 2 --> 3 --> None (after 2 rotations) --> Ans

# For k rotations, k nodes from the back are put in the front and (n-k) nodes follow

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
        while cur_node.next:
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


    def rotate_linked_list(self, k):
        n = self.lengthList()
        print(n)
        k = k % n
        start_node = self.head
        cur = self.head
        
        # find node which is at k'th position from the end
        i = 0
        kthNode = self.head

        while i < n-k-1 and cur.next:
            cur = cur.next
            i+= 1
        prev = cur
        kthNode = prev.next

        while cur.next:
            cur = cur.next  # cur now points to last node in llist
        
        self.head = kthNode 
        cur.next = start_node
        prev.next = None




if __name__ == '__main__':
    llist = LinkedList()
    llist.append("1")
    llist.append("2")
    llist.append("3")
    llist.append("4")
    llist.append("5")
    
    k = int(input())
    
    print("Original Linked List:")
    llist.print_list()
    
    llist.rotate_linked_list(k)
    print("Rotated linked list")
    llist.print_list()

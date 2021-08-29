# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP:
# How would you solve this problem if a temporary buffer is not allowed?

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

    # Space = O(n) and Time = O(n)
    def remove_dups(self):
        # dict to store elements and count as in LL
        cur = self.head
        prev = None
        duplicates = dict()
        # Traversing through the LL to store in duplicates dict
        while cur:
            if cur.data in duplicates:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                duplicates[cur.data] = 1
                prev = cur
            cur = prev.next

        # If no temporary buffer is allowed, 2 pointers cur and run can be used to traverse the list.
        # The cur node remains fixed but run iterates through the entire LL checking other nodes with cur.
        # Space = O(1) and Time = O(n^2) 
        def remove_dups2(self):
            cur = self.head
            while cur:
                run = cur
                if (run.next.data == cur.data):
                    run.next = run.next.next
                else:
                    run = run.next
        
        
        
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("B")
llist.append("D")
print("Original LL:")
llist.print_list()
llist.remove_dups()
print("LL with duplicates removed:")
llist.print_list()


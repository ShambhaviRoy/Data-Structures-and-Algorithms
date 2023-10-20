# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP:
# How would you solve this problem if a temporary buffer is not allowed?

from linked_list import LinkedList 

# Space = O(n) and Time = O(n)
def remove_dups(l1):
    # list to store elements and count as in LL
    cur = l1.head
    prev = None
    data_list = []
    # Traversing through the LL to store in data_list list
    while cur:
        if cur.data in data_list:
            # Remove node
            prev.next = cur.next
            cur = None
        else:
            # Have not encountered element before
            data_list.append(cur.data)
            prev = cur
        cur = prev.next

# If no temporary buffer is allowed, 2 pointers cur and run can be used to traverse the list.
# The cur node remains fixed but run iterates through the entire LL checking other nodes with cur.
# Space = O(1) and Time = O(n^2) 
def remove_dups2(l1):
    cur = l1.head
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
remove_dups(llist)
print("LL with duplicates removed:")
llist.print_list()


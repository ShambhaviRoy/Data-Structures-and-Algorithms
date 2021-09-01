# Loop detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier)
# Output: C

from linked_list import LinkedList

def find_beg(l1):
    slow = l1.head
    fast = l1.head
    while (fast != None) and (fast.next != None):
        fast = fast.next.next
        slow = slow.next 
        if fast is slow:
            break
    
    if fast is None and fast.next is None:
        return None
    
    slow = l1.head
    
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("B")
llist.append("D")
print("Original LL:")
llist.print_list()
ans = find_beg(llist)
print(ans) 
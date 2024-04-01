# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


from linked_list import LinkedList 

def partition(ll, x):
    cur = ll.head
    # LLs to store two parts
    left = LinkedList()
    right = LinkedList()
    
    # Appending nodes to left and right LL
    while cur:
        if cur.data < x:
            left.append(cur.data)
        else:
            right.append(cur.data) 
        cur = cur.next
    
    # Merging both left and right
    left_head = left.head
    while left_head:
        if left_head.next == None: # last node of left LL found
            left_head.next = right.head
        left_head = left_head.next
    return left


llist = LinkedList()
llist.append(3)
llist.append(5)
llist.append(8)
llist.append(5)
llist.append(10)
llist.append(2)
llist.append(1)
l1 = partition(llist, 5)
l1.print_list()

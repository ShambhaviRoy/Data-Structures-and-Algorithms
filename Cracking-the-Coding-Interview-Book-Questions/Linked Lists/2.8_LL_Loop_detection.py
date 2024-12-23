# Loop detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier)
# Output: C

from linked_list import *

def loop_detection_with_set(head):
    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None


def loop_detection(l1):
    slow = l1
    fast = l1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next 
        if fast is slow:
            break
    
    if not fast and not fast.next:
        return None
    
    slow = l1
    
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


def create_ll(arr, node_map):
    ll = Node('*')
    dummy = ll
    for val in arr:
        if val in node_map:
            node = node_map[val]
        else:
            node = Node(val)
            node_map[val] = node
        dummy.next = node
        dummy = dummy.next
    return ll.next


llist = create_ll(['A', 'B', 'C', 'D', 'E', 'C'], {})
ans1 = loop_detection_with_set(llist)
ans1.print_node()
ans2 = loop_detection(llist)
ans2.print_node()
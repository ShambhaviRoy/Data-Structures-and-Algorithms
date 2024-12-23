# Given two (singly) linked lists, determine if the two lists intersect. 
# Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
#linked list, then they are intersecting

from linked_list import *


# Approach 1: Using extra space  
# Time Complexity = O(m + n), Space Complexity = O(m), m = len(l1), n = len(l2)
def intersection_with_set(l1, l2):
    if not l1 or not l2:
        return None
    visited = set()
    while l1:
        visited.add(l1)
        l1 = l1.next
    while l2:
        if l2 in visited:
            return l2
        l2 = l2.next
    return None
    

# Approach 2: Without using extra space
# Time Complexity = O(m + n), Space Complexity = O(1)
def intersection(l1, l2):
    len1, tail1 = get_length_and_tail(l1)
    len2, tail2 = get_length_and_tail(l2)
    if tail1 != tail2:
        return None
    longer = l1 if len1 > len2 else l2
    shorter = l1 if len1 <= len2 else l2
    diff = abs(len1 - len2)
    while diff > 0:
        longer = longer.next
        diff -= 1
    while longer and shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


def get_length_and_tail(head):
    length = 0
    tail = head
    while tail:
        length += 1
        tail = tail.next
    return length, tail

    
    
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


node_map = {}
l1 = create_ll([7, 1, 6, 5, 2, 3], node_map)
l2 = create_ll([4, 8, 5, 2, 3], node_map)


ans1 = intersection_with_set(l1, l2)
ans1.print_node()

ans2 = intersection(l1, l2)
if intersection(l1, l2) == None:
    print('No intersection')
else:
    print('Intersection')
    ans2.print_node()

         
        
            
        
        
        
            
        

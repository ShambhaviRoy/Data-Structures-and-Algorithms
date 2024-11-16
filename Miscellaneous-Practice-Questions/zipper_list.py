# https://structy.net/problems/zipper-lists

# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.
# Do this in-place, by mutating the original Nodes.
# You may assume that both input lists are non-empty.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# helper methods
def print_list(head):
    while head:
        print(head.val, end = ' ')
        head = head.next
        
def linked_list_from_array(arr):
    head = Node('*')
    list1 = head
    for num in arr:
        list1.next = Node(num)
        list1 = list1.next
    return head.next


# Iterative approach
# Time Complexity = O(n), Space Complexity = O(1)
def zipper_list(head1, head2):
    curr1 = head1.next
    curr2 = head2
    tail = head1
    count = 0
    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1
    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return head1



# Recursive
def zipper_list_recursive(head1, head2):
    if not head1 and not head2:
        return None
    if not head1:
        return head2
    if not head2:
        return head1
    nxt1 = head1.next
    nxt2 = head2.next
    head1.next = head2
    head2.next = zipper_list_recursive(nxt1, nxt2)
    return head1
    



head1 = linked_list_from_array(['a', 'b', 'c', 'd', 'e', 'f'])
head2 = linked_list_from_array(['x', 'y', 'z'])
# zipped = zipper_list(head1, head2)
# print_list(zipped)

zipped2 = zipper_list_recursive(head1, head2)
print_list(zipped2)
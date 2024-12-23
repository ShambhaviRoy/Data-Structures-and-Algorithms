# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# FOLLOW UP: Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output: 9 - > 1 - > 2. That is, 912.


# Approach:
# Digits have to line up correctly to add --> pad shorter list with 0s in the front
# Add the 2 lists iteratively and keep adding to the back of the result list

from linked_list import *


class PartialSum:
    def __init__(self):
        self.sum = Node('*')
        self.carry = 0

def insert_before(head, value):
    node = Node(value)
    node.next = head
    return node


def pad_list(head, spots, value):
    l = head
    for _ in range(spots):
        l = insert_before(l, value)
    return l


def add_lists(l1, l2):
    len1 = length_of_list(l1)
    len2 = length_of_list(l2)

    if len1 > len2:
        l2 = pad_list(l2, len1 - len2, 0)
    else:
        l1 = pad_list(l1, len2 - len1, 0)

    total = add_lists_helper(l1, l2)
    if total.carry == 0:
        return total.sum
    else:
        result = insert_before(total.sum, total.carry)
        return result

    
def add_lists_helper(l1, l2):
    if not l1 and not l2:
        return PartialSum()
    total = add_lists_helper(l1.next, l2.next)
    val = total.carry + l1.data + l2.data
    full_result = insert_before(total.sum, val % 10)
    total.sum = full_result
    total.carry = val // 10
    return total
    
    


l1 = create_linked_list_from_array([1, 2, 3, 4])
l2 = create_linked_list_from_array([5, 6, 7])
ans = add_lists(l1, l2)
print_list(ans)
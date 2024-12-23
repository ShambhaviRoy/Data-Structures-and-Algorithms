# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .That is,617 + 295.
# Output: 2 - > 1 - > 9. That is, 912.

from linked_list import Node
from linked_list import *

# Approach 1: Extract numbers from both lists and simply add them
def sum_lists(l1, l2):
    # Extract num1 from l1
    cur = l1.head
    i = 0
    num1 = 0
    while cur:
        num1 += (cur.data)*10**(i)
        i += 1
    # Extract num2 from l2
    cur = l2.head
    i = 0
    num2 = 0
    while cur:
        num2 += (cur.data)*10**(i)
        i += 1
    # Sum
    ans = num1 + num2
    # Put ans in a LL
    lans = Node('*')
    dummy = lans
    while ans > 0:
        digit = ans % 10
        ans = ans / 10
        dummy.next = Node(digit)
        dummy = dummy.next
    return lans.next

# Approach 2: Recursive: When the 1s digit is at the head of the list
#  7 -> 1 -> 6
# +5 -> 9 -> 2
# 7 + 5 = 12, value = 2, carry = 1
def addLists(l1, l2, carry):
    if l1 is None and l2 is None and carry == 0:
        return None
    result = Node('*')
    dummy = result
    value = carry
    if l1:
        value += l1.data
    if l2:
        value += l2.data
    digit = value % 10
    dummy.next = Node(digit)
    dummy = dummy.next
    if l1 != None or l2 != None:
        more = addLists(l1.next, l2.next, 1 if value >= 10 else 0)
        dummy.next = more
    return result.next


# Approach 3: Iterative: When the 1s digit is at the head of the list
def addLists1(l1, l2):
    result = Node('*')
    dummy = result

    curr1 = l1
    curr2 = l2
    carry = 0
    while curr1 and curr2:
        total = curr1.data + curr2.data + carry
        carry = total // 10
        total = total % 10
        dummy.next = Node(total)
        dummy = dummy.next
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 and not curr2:
        total = curr1.data + carry
        carry = total // 10
        total = total % 10
        dummy.next = Node(total)
        dummy = dummy.next

    if curr2 and not curr1:
        total = curr2.data + carry
        carry = total // 10
        total = total % 10
        dummy.next = Node(total)
        dummy = dummy.next

    if carry != 0:
        dummy.next = Node(carry)
        dummy = dummy.next


    return result.next





print('Recursive: When the 1s digit is at the head of the list')
l1 = create_linked_list_from_array([7, 1, 6])
l2 = create_linked_list_from_array([5, 9, 2])
ans1 = addLists(l1, l2, 0)
print_list(ans1)

print('Iterative: When the 1s digit is at the head of the list')
l1 = create_linked_list_from_array([7, 1, 6])
l2 = create_linked_list_from_array([5, 9, 2])
ans2 = addLists1(l1, l2)
print_list(ans2)

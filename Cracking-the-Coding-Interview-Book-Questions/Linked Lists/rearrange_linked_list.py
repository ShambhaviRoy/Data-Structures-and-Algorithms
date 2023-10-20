# Suppose you had a linked list a1 -> a2 -> ••• -> an ->b1 -> b2 -> ••• ->bn and you wanted to rearrange it into 
# a1 -> b1 -> a2 -> b2 -> •.• -> an-> bn
# You do not know the length of the linked list (but you do know that the length is an even number).


from linked_list import LinkedList

def rearrange_ll(llist):

    if not llist.head or llist.head.next:
        return llist

    fast = llist.head
    slow = llist.head
    curr = llist.head

    # fast pointer moves 2 steps ahead, while slow pointer moves 1 step ahead
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # now rearrange, start iterating from slow
    while slow and slow.next:
        slow.next = curr.next
        curr.next = slow
        curr = curr.next
        slow = slow.next


    return llist

    

llist = LinkedList()
llist.append("a1")
llist.append("a2")
llist.append("a3")
llist.append("b1")
llist.append("b2")
llist.append("b3")
print("Original LL:")
llist.print_list()
rearrange_ll(llist)
print("Rearranged LL:")
llist.print_list()
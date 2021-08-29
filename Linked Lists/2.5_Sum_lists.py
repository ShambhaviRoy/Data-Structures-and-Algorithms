# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .That is,617 + 295.
# Output: 2 - > 1 - > 9. That is, 912.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # If the LL is empty
        if self.head is None:
            self.head = new_node
            return
        # If LL is not empty
        last_node = self.head
        while last_node:
            if last_node.next:
                last_node = last_node.next
                last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def sum_lists(self, l2):
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
        lans = LinkedList()
        while ans > 0:
            digit = ans % 10
            ans = ans / 10
            lans.append(digit)
        return lans

        # BETTER APPROACHES
        #  7 -> 1 -> 6
        # +5 -> 9 -> 2
        # 7 + 5 = 12, value = 2, carry = 1
        def addLists(self, l2, carry):
            if self == None or l2 == None or carry == None:
                return None
            result = LinkedList()
            value = carry
            cur = self.head
            while cur:
                value += cur.data 
            cur = l2.data
            while cur:
                value += cur.data 
            result.data = value % 10
            #if l1 != None or l2 != None:



l1 = LinkedList()
l1.append(7)
l1.append(1)
l1.append(6)

l2 = LinkedList()
l2.append(5)
l2.append(9)
l2.append(2)

ans = l1.sum_lists(l2)
ans.print_list()



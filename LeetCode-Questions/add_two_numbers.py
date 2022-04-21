# Function to add 2 numbers in linked list format
# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        
        dummyHead = ListNode(0)
        curr = dummyHead
        
        x, y, add, carry = 0, 0, 0, 0
        
        while p or q or carry:
            x = (p.val if p else 0)
            y = (q.val if q else 0)
            
            carry, add = divmod(x + y + carry, 10)
            
            curr.next = ListNode(add)
            curr = curr.next
            
            p = (p.next if p else None)
            q = (q.next if q else None)
            
        return dummyHead.next

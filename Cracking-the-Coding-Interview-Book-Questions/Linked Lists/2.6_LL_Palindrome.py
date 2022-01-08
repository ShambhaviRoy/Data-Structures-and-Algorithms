from linked_list import LinkedList

def palindrome1(l1):
    s = ""
    cur = l1.head
    while cur:
        s += str(cur.data)
        cur = cur.next
    return (s == s[::-1])

def palindrome2(l1):
    s = []
    cur = l1.head
    while cur:
        s.append(cur.data)
    while cur:
        if cur.data != s.pop():
            return False
    return True


llist = LinkedList()
llist.append(0)
llist.append(1)
llist.append(2)
llist.append(1)
llist.append(0)
print(palindrome1(llist))
print(palindrome2(llist))

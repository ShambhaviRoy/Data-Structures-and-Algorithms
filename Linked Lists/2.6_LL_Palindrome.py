class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendList(self, data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def palindrome1(self):
        s = ""
        cur = self.head
        while cur:
            s += str(cur.data)
            cur = cur.next
        return (s == s[::-1])

    def palindrome2(self):
        s = []
        cur = self.head
        while cur:
            s.append(cur.data)
        while cur:
            if cur.data != s.pop():
                return False
        return True

llist = LinkedList()
llist.appendList(0)
llist.appendList(1)
llist.appendList(2)
llist.appendList(1)
llist.appendList(0)
print(llist.palindrome1())
print(llist.palindrome2())

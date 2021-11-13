class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def append(self, data):     #insert element at the end of linked list
        new_node = Node(data)

        #if linked list is empty
        if self.head is None:
            self.head = new_node
            return

        #if linked list is not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):    #insert element at the beginning of linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        #to delete head node
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        #to delete node other than head
        prev = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        #to delete node at position 0
        cur_node = self.head
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
        #to delete any other node
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    #Calculate length of list
    #Iterative approach
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    #Recursive approach
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    #Swap 2 nodes whose keys(data values) are given
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return

        #swap
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    #Reverse linked list
    #Iterative implementation (changing direction of arrows)
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    #Recursive implementation 
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    #Merge 2 sorted linked lists
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
            while p and q:
                if p.data <= q.data:
                    s.next = p 
                    s = p 
                    p = s.next
                else:
                    s.next = q
                    s = q
                    q = s.next
            if not p:
                s.next = q 
            if not q:
                s.next = p 
            return new_head

    #Helper function
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    #remove duplicate elements from Linked List
    def remove_duplicates(self):
        cur = self.head
        prev = None
        duplicates = dict()
        while cur:
            if cur.data in duplicates:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                duplicates[cur.data] = 1
                prev = cur
            cur = prev.next

    #Print node at nth from last position
    def print_nth_from_last(self, n, method):
        if method == 1:
            #Calculate length of LL and count down until n is reached
            total_len = self.len_iterative()
            cur = self.head
            while cur:
                if total_len == n:
                    #print(cur.data)
                    return cur.data
                    total_len += -1
                    cur = cur.next
                if cur is None:
                    return 

        elif method == 2:
            #Pointers: p=head, q=n+head, when q=None, p=ans
            p = self.head
            q = self.head
            #set q at n steps ahead of head
            count = 0
            while q:
                count += 1 
                if (count >= n):
                    break
                q = q.next
            if not q:
                print(n, " is greater than length of list.")
                return
            #list traversal
            while p and q.next:
                p = p.next
                q = q.next
            return p.data

        else:
            return 

    #Count occurrences of element in a linked list
    def count_occurrences_iterative(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    #Rotate linked list about a specified pivot element
    def rotate(self, k):
        # the list is rotated around kth element
        # checking if the element has more than 1 node
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count < k:
            prev = p 
            p = p.next
            q = q.next
            count += 1
        p = prev    #so far, p is set at the pivot node
        while q:
            prev = q
            q = q.next
        q = prev    # q is now set to the end of linked list

        q.next = self.head
        self.head = p.next
        p.next = None

    #To check if the linked list is a palindrome-read same from front and back
    #Approach 1:
    def is_palindrome_1(self):
        cur = self.head
        s = ""
        while cur:
           s += cur.data
           cur = cur.next
        return s == s[::-1]

    #Approach 2:
    def is_palindrome_2(self):
        cur = self.head
        s = []
        while cur:
            s.append(cur.data)
            cur = cur.next
        cur = self.head
        while cur:
            data = s.pop()
            if cur.data != data:
                return False
            cur = cur.next
        return True

    #Approach 3
    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
                q = prev[i-1]

            count = 1
            while count <= i//2 +1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self, method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()
        else:
            return

    #Move tail node to head and shift all other nodes right
    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head 
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head 
            second_to_last.next = None 
            self.head = last

    #Sum two linked lists
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s>=10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist 


#FUNCTION CALLS
#create new LL and append values to it
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
#prepended in list
llist.prepend("D")

print("The list is:")
llist.print_list()  

#inserting a value
llist.insert_after_node(llist.head.next, "E")
print("Added E after node next to head(A):")
llist.print_list()

llist.delete_node("B")
print("Deleted B:")
llist.print_list()

print("Length of list(iterative approach):")
print(llist.len_iterative())

print("Length of whole list(recursive approach):")
print(llist.len_recursive(llist.head))

print("Original List:")
print(llist.print_list())

llist.swap_nodes("A", "E")
print("List after swapping nodes A and E, none of them head:")
print(llist.print_list())

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()

llist_3 = LinkedList()
llist_3.append(1)
llist_3.append(6)
llist_3.append(1)
llist_3.append(4)
llist_3.append(2)
llist_3.append(2)
llist_3.append(4)

print("Original Linked List:")
llist_3.print_list()
print("Linked List After Removing Duplicates:")
llist_3.remove_duplicates()
llist_3.print_list()

llist_4 = LinkedList()
llist_4.append("A")
llist_4.append("B")
llist_4.append("C")
llist_4.append("D")
print("Linked List:")
llist_4.print_list()
print("From method 1:")
print(llist_4.print_nth_from_last(4,1))
print("From method 2:")
print(llist_4.print_nth_from_last(4,2))

llist_5 = LinkedList()
llist_5.append(1)
llist_5.append(2)
llist_5.append(3)
llist_5.append(4)
llist_5.append(5)
llist_5.append(6)
print("First list:")
print(llist_5.print_list())

llist_6 = LinkedList()
llist_6.append(1)
llist_6.append(2)
llist_6.append(1)
llist_6.append(3)
llist_6.append(1)
llist_6.append(4)
llist_6.append(1)
print("Second list:")
print(llist_6.print_list())
print(llist_6.count_occurrences_iterative(1))
print(llist_6.count_occurrences_recursive(llist_6.head, 1))

llist_7 = LinkedList()
llist_7.append(1)
llist_7.append(2)
llist_7.append(3)
llist_7.append(4)
llist_7.append(5)
llist_7.append(6)
print("Linked list:")
print(llist_7.print_list())
llist_7.rotate(4)
print("Rotated list:")
llist_7.print_list()

# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist_8 = LinkedList()

llist_8 = LinkedList()
llist_8.append("A")
llist_8.append("B")
llist_8.append("C")

print(llist_8.is_palindrome(1))
print(llist_8.is_palindrome(2))
print(llist_8.is_palindrome(3))

llist_9 = LinkedList()
llist_9.append('A')
llist_9.append('B')
llist_9.append('C')
llist_9.append('D')
print(llist_9.move_tail_to_head())


llist_10 = LinkedList()
llist_10.append(5)
llist_10.append(6)
llist_10.append(3)

llist_11 = LinkedList()
llist_11.append(8)
llist_11.append(4)
llist_11.append(2)

print(365 + 248)
llist_11.sum_two_lists(llist_10)

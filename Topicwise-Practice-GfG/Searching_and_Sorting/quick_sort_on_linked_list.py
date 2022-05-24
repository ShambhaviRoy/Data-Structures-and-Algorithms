# Perform Quick Sort on Linked List

# For Singly linked list
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


    def partition(self, start, end):
        # Find the pivot in list having start and end nodes
        # Iterate from start to end --> return one before prev
        
        if start == end or start == None or end == None:
            return start

        pivot_prev = start
        curr = start
        pivot = end.data

        while start != end:
            if start.data < pivot:
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next

        temp = curr.data
        curr.data = pivot
        end.data = temp

        return pivot_prev


    def quick_sort_recur(self, start, end):
        # Find pivot and recurse on left and right part of the list
        # Left part: start to pivot_prev
        # Right part: pivot_prev.next to end

        if start == None or start == end or start == end.next:
            return 

        pivot_prev = self.partition(start, end)
        self.quick_sort_recur(start, pivot_prev)    # recursing on left part

        if pivot_prev != None and pivot_prev == start:
            self.quick_sort_recur(pivot_prev.next, end) # recursing on right part
            
        elif pivot_prev != None and pivot_prev.next != None:
            self.quick_sort_recur(pivot_prev.next.next, end)


llist_1 = LinkedList()

llist_1.append(1)
llist_1.append(9)
llist_1.append(8)
llist_1.append(52)
llist_1.append(7)
llist_1.append(20)
llist_1.append(40)

print("The given list is:")
llist_1.print_list()  

n = llist_1.head
while n.next != None:
    n = n.next

llist_1.quick_sort_recur(llist_1.head, n)

print("The sorted list is:")
llist_1.print_list()  

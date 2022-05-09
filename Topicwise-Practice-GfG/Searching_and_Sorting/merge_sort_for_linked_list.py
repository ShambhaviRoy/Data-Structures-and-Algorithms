# Perform Merge Sort for Singly Linked List
# Keep splitting the linked list - sort the parts and finally merge the sorted parts
# the left and right parts are sorted recursively 
# To find the parts- find the middle of the linked list

# Time Complexity = O(n log n), Space Complexity = O(n log n)


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


    def merge_sort(self, head):
        # Edge cases : If given head is None OR list has only 1 element, return the head of linked list
        if head == None or head.next == None:
            return head

        # get the middle of the linked list
        middle = self.get_middle_list(head)
        next_to_middle = middle.next
        middle.next = None

        # split the list into 2 parts: left_part and right_part
        # left_part has nodes from head to middle
        # right_part has nodes from next_to_middle to None at the end
        # perform merge_sort recursively on these parts
        left_part = self.merge_sort(head)
        right_part = self.merge_sort(next_to_middle)

        # the final answer is formed by merging the sorted left_part and right_part
        sorted_list = self.sorted_merge(left_part, right_part)
        return sorted_list


    def get_middle_list(self, head):    # function to find middle of linked list
        if head == None:
            return head
        
        start = head
        end = head

        while end.next != None and end.next.next != None:
            start = start.next
            end = end.next.next

        return start


    def sorted_merge(self, left_head, right_head):          # function to merge the sorted left_part and right_part
        result = None

        while left_head == None:
            return right_head

        while right_head == None:
            return left_head

        # choose node from left or right depending on value
        # then recurse to continue merging
        if left_head.data <= right_head.data:
            result = left_head
            result.next = self.sorted_merge(left_head.next, right_head)
        else:
            result = right_head
            result.next = self.sorted_merge(left_head, right_head.next)

        return result


    

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(40)
    llist.append(20)
    llist.append(60)
    llist.append(10)
    llist.append(50)
    llist.append(30)

    print("The given list is:")
    llist.print_list()  
    print('-'*20)

    llist.head = llist.merge_sort(llist.head)
    print("The sorted list is:")
    llist.print_list()  
    print('-'*20)

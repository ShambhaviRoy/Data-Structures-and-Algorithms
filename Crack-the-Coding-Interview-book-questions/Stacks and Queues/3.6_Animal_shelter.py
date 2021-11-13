class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
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

            
    def lengthList(self):
        cur = self.head 
        length = 0
        while cur:
            length += 1
            cur = cur.next 
        return length
    
    
    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head 
            self.head = self.head.next
        return head_to_pop
    
    
    
class Animal:
    def __init__(self, order):
        self.order = order
        
class Cat(Animal):
    pass

class Dog(Animal):
    pass
    
class AnimalShelter(LinkedList):
    def dequeue(self, animal):
        animal_node = Node(animal)
        self.append(animal_node)
        
    def dequeue_any(self):
        return super().pop_head()
    
    def dequeue_cat(self):
        prev = None
        cur = self.head 
        while cur:
            if cur.data == 'cat':
                prev.next = cur.next
                return cur.data
            prev = cur 
            cur = cur.next
        return None
    
    def dequeue_dog(self):
        prev = None
        cur = self.head 
        while cur:
            if cur.data == 'dog':
                prev.next = cur.next
                return cur.data
            prev = cur 
            cur = cur.next
        return None
    
    
                
        
        

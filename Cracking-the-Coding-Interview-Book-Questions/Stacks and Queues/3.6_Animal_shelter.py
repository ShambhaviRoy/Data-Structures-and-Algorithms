# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in LinkedList data structure.

        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):     #insert element at the end of linked list
        new_node = Animal(data)
        #if linked list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = None
        else:
            #if linked list is not empty
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.next = None

            
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
    

    def print_list(self):
        curr = self.head
        while curr:
            curr.print_animal()
            curr = curr.next


    def is_empty(self):
        return self.lengthList() == 0
    
    
# Implement Animal Shelter queue using LinkedList

import time

class Animal:
    def __init__(self, type):
        self.type = type
        self.timestamp = time.time()

    def animal_data(self):
        return (self.type, self.timestamp)

    def is_older_than(self, other):
        return self.timestamp < other.timestamp
    
    def print_animal(self):
        print(f'Type = {self.type}, Timestamp = {self.timestamp}')


class Dog(Animal):
    def __init__(self):
        self.type = 'Dog'
        self.timestamp = time.time()


class Cat(Animal):
    def __init__(self):
        self.type = 'Cat'
        self.timestamp = time.time()


class AnimalShelter():
    def __init__(self):
        self.dog_queue = LinkedList()
        self.cat_queue = LinkedList()


    def enqueue(self, animal):
        if animal == 'Dog':
            dog = Dog()
            self.dog_queue.append(dog.type)
        elif animal == 'Cat':
            cat = Cat()
            self.cat_queue.append(cat.type)
        else:
            raise Exception('Undefined operation')
        

    def dequeueAny(self):
        # find the oldest animals and dqueue the older one
        if(self.dog_queue.is_empty()):
            return self.cat_queue.head
        elif (self.cat_queue.is_empty()):
            return self.dog_queue.head
        oldest_dog = self.dog_queue.head
        oldest_cat = self.cat_queue.head
        flag = oldest_dog.is_older_than(oldest_cat)
        if flag:
            return self.dequeueDog()
        else:
            return self.dequeueCat()
        

    def dequeueDog(self):
        return self.dog_queue.pop_head()

    def dequeueCat(self):
        return self.cat_queue.pop_head()
    

    def print_shelter(self):
        shelter.dog_queue.print_list()
        shelter.cat_queue.print_list()



animals = ['Dog', 'Cat', 'Dog', 'Dog', 'Cat', 'Cat', 'Dog']
shelter = AnimalShelter()

for animal in animals:
    shelter.enqueue(animal)

# check shelter
print('Animals in shelter:')
shelter.print_shelter()


print('---')
oldest_animal = shelter.dequeueAny()
print('Oldest animal:')
oldest_animal.print_animal()

print('---')
oldest_dog = shelter.dequeueDog()
print('Oldest dog:')
oldest_dog.print_animal()

print('---')
oldest_cat = shelter.dequeueCat()
print('Oldest cat:')
oldest_cat.print_animal()
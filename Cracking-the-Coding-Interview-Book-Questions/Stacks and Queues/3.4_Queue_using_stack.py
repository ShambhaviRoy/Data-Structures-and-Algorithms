from stack import Stack

class MyQueue:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()
        
    
    def size(self):
        return len(self.stack_new.items) + len(self.stack_old.items)
    
    
    def is_empty(self):
        return self.stack_new.is_empty()
    
    
    def shift_stacks(self):
        if self.stack_old.is_empty():
            while not self.stack_new.is_empty():
                self.stack_old.push(self.stack_new.pop())
            
    
    def add(self, item):
        self.stack_new.push(item)
        
    
    def remove(self):
        self.shift_stacks()
        return self.stack_old.pop()
        
    
    def peek(self):
        self.shift_stacks()
        return self.stack_old.peek()
    
    def print_stacks(self):
        print(f'old stack = {[x for x in self.stack_old.items]}, new stack = {[x for x in self.stack_new.items]}')

    
q = MyQueue()
q.add(2)
q.add(4)
q.add(6)
q.add(8)
q.add(10)
q.add(12)
print(q.size())

q.print_stacks()
q.remove()
q.print_stacks()

print(q.peek())
q.print_stacks()

q.remove()
print(q.size())

q.add(14)
q.print_stacks()

q.remove()
q.print_stacks()

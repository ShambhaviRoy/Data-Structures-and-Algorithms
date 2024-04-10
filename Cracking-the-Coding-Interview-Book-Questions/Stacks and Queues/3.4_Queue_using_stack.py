from stack import Stack

class MyQueue:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()
        
    
    def size(self):
        return len(self.stack_new) + len(self.stack_old)
    
    
    def is_empty(self):
        return self.stack_new.is_empty()
    
    
    def shift_stacks(self):
        if self.stack_old.is_empty():
            self.stack_old.push(self.stack_new.pop())
            
    
    def add(self, item):
        self.stack_new.push(item)
        
    
    def remove(self):
        self.shift_stacks()
        return self.stack_old.pop()
        
    
    def peek(self):
        self.shift_stacks()
        return self.stack_old.peek()
        
    
q = MyQueue()
q.add(4)
q.add(6)
print(str(q.size))
q.remove()
q.remove()
print(str(q.size))
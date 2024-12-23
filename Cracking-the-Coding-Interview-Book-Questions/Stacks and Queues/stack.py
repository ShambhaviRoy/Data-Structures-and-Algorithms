class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
        
    
    def push(self, item):
        self.items.append(item)
        self.size += 1
        
   
    def pop(self):
        if self.size >= 1:
            element = self.items.pop()
            self.size -= 1
        return element
    
    
    def is_empty(self):
        return len(self.items) == 0
    
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
        
    def print_stack(self):
        while self.items:
            print(self.peek())
            self.pop()

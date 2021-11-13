class Stack:
    def _init_(self, items):
        self.items = []
        self.size = 0
        
    
    def push(self, item):
        self.items.append(item)
        self.size += 1
        
   
    def pop(self):
        self.size -= 1
        return self.items.pop()
    
    
    def is_empty(self):
        return len(self.items) == 0
    
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
        

from stack import Stack

class SortStack:
    def __init__(self):
        super().__init__()
        # self.stack = Stack()
        self.buffer = Stack()
        
    def sort_stack(self, stack):
        while not stack.is_empty():
            #insert elements into buffer
            temp = stack.pop()
            while (not self.buffer.is_empty() and self.buffer.peek() > temp):
                stack.push(self.buffer.pop()) 
            self.buffer.push(temp)
            
        # buffer elements to stack
        while not self.buffer.is_empty():
            stack.push(self.buffer.pop())
            
        return stack
        
    
s = Stack()
s.push(1)
s.push(12)
s.push(5)
s.push(3)
s.push(7)  

sorted_s = sort_stack(s)
sorted_s.pop()
from stack import Stack

class setofStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.set = []
        
    
    def isEmpty(self):
        last = self.getLastStack()
        return not last or last.is_empty()
    
    def isFull(self):
        return not(self.isEmpty)

    
    def getLastStack(self):
        if self.set:
            return self.set[-1]
    
    
    def push(self, item):
        # get last stack
        # push element to last stack
        # if last stack is full --> make new stack
        last = self.getLastStack()
        if last and not last.isFull():
            last.push(item)
        else:
            stack = Stack(self.capacity)
            stack.push(item)
            self.set.append(stack)
        
   
    def pop(self):
        # get last stack
        # pop item from last stack
        last = self.getLastStack()
        if not last:
            return None
        
        # if size of last stack == 0 --> remove last from set
        if last.size == 0:
            del self.set[:-1]
        return last.pop()
        
    
    # Followup: implement popAt(index) to remove an item from a specific substack (indexed)
    def popAt(self, index, removeTop):
        stack = self.set[index]
        if removeTop:
            return stack.pop()
        elif stack.is_empty():
            del self.set[index]
        
            
        
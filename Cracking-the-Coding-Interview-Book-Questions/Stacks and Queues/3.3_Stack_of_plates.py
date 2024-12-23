class Stack:
    def __init__(self, threshold):
        self.threshold = threshold
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        if self.elements:
            self.elements.pop()
        return None
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def is_full(self):
        return len(self.elements) == self.threshold
    
    def size(self):
        return len(self.elements)




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
        if last and not last.is_full():
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
        if stack.is_empty():
            del self.set[index]

    def print_set(self):
        for stack in self.set:
            print([x for x in stack.elements])
        
            
        
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 3

stackSet = setofStacks(3)

for val in arr:
    stackSet.push(val)
    

stackSet.print_set()
print('---')

stackSet.pop()
stackSet.print_set()
print('---')

stackSet.popAt(1, True)
stackSet.print_set()
print('---')
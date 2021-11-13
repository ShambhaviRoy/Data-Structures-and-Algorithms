# Implement 3 stacks using an array
# Solution: Implemented 3 stacks of fixed size in an array 
# array = [stack0, stack1, stack2]


class FixedMultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [0] * (self.stack_size * 3)
        self.sizes = [0] * 3
        self.capacity = [self.stack_size] * 3
        
    
    def push(self, item, stack_num):
        if stack_num >= 3:
            return None
        else:
            self.sizes[stack_num] += 1
            self.array[self.index_of_top(stack_num)] = item
                       
    
    def pop(self, stack_num):
        if stack_num > 3:
            return None
        else:
            value = self.array[self.index_of_top(stack_num)]
            self.array[self.index_of_top(stack_num)] = 0
            self.sizes[stack_num] -= 1
            return value
    
    
    def peek(self, stack_num):
        return self.array[self.index_of_top(stack_num)]
        
        
    
    def isEmpty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    
    def index_of_top(self, stack_num):
         offset = stack_num * self.stack_size
         return offset + self.sizes[stack_num] - 1
    
        
    
if __name__ == "__main__":
    newstack = FixedMultiStack(3)
    print(newstack.array)
    print(newstack.isEmpty(1))
    
    newstack.push(2, 0)
    newstack.push(2, 0)
    newstack.push(3, 1)
    newstack.push(3, 1)
    newstack.push(4, 2)
    newstack.push(4, 2)
    newstack.push(5, 2)
    print(newstack.array)
    
    print(newstack.peek(1))
    print(newstack.isEmpty(1))
    
    newstack.push(2, 1)
    print(newstack.array)
    
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    
    newstack.push(3, 1)
    print(newstack.array)
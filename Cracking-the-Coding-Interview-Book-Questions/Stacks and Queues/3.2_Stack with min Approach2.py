from stack import Stack

# Approach 2: Keep 1 stack with the values and another stack with minimums
# Because the minimums don't change often
# Each method is O(1)

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.minvals = Stack()
        
    def minimum(self):
        min_found = self.minvals.peek()
        return min_found if min_found else float('inf')
    
    def push(self, item):
        self.stack.push(item)
        if item <= self.minimum():
            self.minvals.push(item)
            
    def pop(self):
        item = self.stack.pop()
        if item == self.minimum():
            self.minvals.pop()
        return item
    


if __name__ == "__main__":
    newstack = MinStack()
    assert newstack.minimum() == float('inf')

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1

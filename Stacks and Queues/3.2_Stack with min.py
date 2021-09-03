from stack import Stack

class MinStack:
    def __init__(self):
        self.minvals = Stack()
        
    def minimum(self):
        return self.minvals.peek()
    
    def push(self, item):
        super().push(item)
        if item <= self.minimum:
            self.minvals.push(item)
            
    def pop(self):
        item = super().pop()
        if item == self.minimum():
            self.minvals.pop()
        return item
    


if __name__ == "__main__":
    newstack = MinStack()
    assert newstack.minimum() is None

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

# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# Approach 1: Keep a stack storing tuple of value and minimum so far
# Each method is O(1)


class StackWithMin:
    def __init__(self):
        self.values = []

    def push(self, data):
        min_so_far = self.min_so_far()
        if data < min_so_far:
            min_so_far = data
        element = (data, min_so_far)
        self.values.append(element)


    def pop(self):
        if self.is_empty():
            return None
        return self.values.pop()


    def min_so_far(self):
        if self.is_empty():
            return float('inf')
        return self.values[-1][1]


    def is_empty(self):
        return len(self.values) == 0
    

    def print_stack(self):
        print(self.values)
    


stack = StackWithMin()
stack.push(5)
print(f'stack min_so_far = {stack.min_so_far()}')

stack.push(6)
print(f'stack min_so_far = {stack.min_so_far()}')

stack.push(3)
stack.print_stack()
print(f'stack min_so_far = {stack.min_so_far()}')

stack.push(7)
print(f'stack min_so_far = {stack.min_so_far()}')
stack.pop()

stack.push(-1)
print(f'stack min_so_far = {stack.min_so_far()}')
stack.print_stack()

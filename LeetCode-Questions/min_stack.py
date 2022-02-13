# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# https://leetcode.com/problems/min-stack/

# Approach: Saving (pushing) the tuple (value, current_min) on the stack
# current_min is the min of all values seen so far
# So while pushing, get min and compare with val to be pushed

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min == None or val < current_min:
            current_min = val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) -1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) -1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(4)
obj.pop()
obj.push(1)
obj.push(6)
print(obj.top())
print(obj.getMin())
class Stack:
    def __init__(self):
        self.items = []

    #to push(insert) an item into stack-it becomes the topmost element of the stack 
    def push(self, item):
        self.items.append(item)

    #to remove the topmost item from stack
    def pop(self):
        return self.items.pop()

    #to return all elements of the stack
    def get_stack(self):
        return self.items

    #to return whether the stack is empty
    def is_empty(self):
        return self.items == []

    #To return the topmost element of the stack (does not remove it from the stack)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

myStack = Stack()
print(myStack.is_empty())
myStack.push("A")
myStack.push("B")
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.peek())
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.is_empty())
print(myStack.peek())

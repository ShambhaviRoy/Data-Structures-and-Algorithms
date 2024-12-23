from stack import Stack

        
def sort_stack(stack):
    buffer = Stack()

    while not stack.is_empty():
        #insert elements into buffer
        temp = stack.pop()
        while (not buffer.is_empty() and buffer.peek() > temp):
            stack.push(buffer.pop()) 
        buffer.push(temp)
        
    # buffer elements to stack
    while not buffer.is_empty():
        stack.push(buffer.pop())
        
    return stack
    
    
s = Stack()
s.push(1)
s.push(12)
s.push(5)
s.push(3)
s.push(7)  

sorted_s = sort_stack(s)

print('Elements in sorted order:')
sorted_s.print_stack()
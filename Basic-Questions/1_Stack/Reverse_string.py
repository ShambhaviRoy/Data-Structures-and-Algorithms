from Stack_data_structure import Stack

def reverse_string(stack, input_string):
    
    #pushing all elements into stack
    for i in range(len(input_string)):
        stack.push(input_string[i])

    rev_str = ''
    for i in range(len(input_string)):
        rev_str+= stack.pop()

    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
    
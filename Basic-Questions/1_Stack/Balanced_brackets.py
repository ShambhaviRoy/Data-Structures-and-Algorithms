from Stack_data_structure import Stack

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '{' and p2 == '}':
        return True
    if p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_paren_balanced(parenString):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parenString) and is_balanced:
        paren = parenString[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        
        index = index + 1

    if s.is_empty and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))

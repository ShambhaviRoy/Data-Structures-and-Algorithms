# Recursive Multiply: Write a recursive function to multiply two positive integers without using
# the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.


def recursive_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    
    bigger = a if a > b else b
    smaller = a if a < b else b
    return bigger + recursive_multiply(bigger, smaller-1)


print(recursive_multiply(5, 4))

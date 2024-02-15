# Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.

def calculate_factorial(n):
    if n == 1:
        return n
    elif n > 1:
        return n * calculate_factorial(n-1)
    else:
        return -1
    
n = 5
n_factorial = calculate_factorial(n)

count_zeros = 0
quotient = n_factorial

while(quotient >= 1):
    remainder = quotient % 10
    if(remainder == 0):
        count_zeros += 1
    quotient = quotient / 10

print(count_zeros)

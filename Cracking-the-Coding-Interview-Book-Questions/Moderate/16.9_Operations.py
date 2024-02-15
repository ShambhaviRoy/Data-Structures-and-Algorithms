# Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
# The results of all of these are integers. Use only the add operator.


def negate(num):
    neg = 0
    new_sign = 1 if num < 0 else -1
    while(num != 0):
        neg += new_sign
        num += new_sign
    return neg


def subtract(num1, num2):
    return num1 + negate(num2)


def multiply(num1, num2):
    if(num1 < num2):
        return multiply(num2, num1)
    ans = 0
    while(num2 > 0):
        ans += num1
        num2 -= 1
    return ans


def divide(num1, num2):
    quotient = 0
    while(num1 > 0):
        num1 = subtract(num1, num2)
        quotient += 1
    return quotient
        
    


print(subtract(24, 9))
print(multiply(5, 4))
print(divide(10, 2))
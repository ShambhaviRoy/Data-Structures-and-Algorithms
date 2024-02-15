# Number Max: Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.

def flip(bit):
    # flips the bit
    return 1 ^ bit

def sign(num):
    # returns 1 if num is +ve and 0 if num is -ve
    return flip((num >> 31) & 1)


# Approach 1: Find the sign of the difference, flip it, add to num2 
def get_max1(num1, num2):
    k = sign(num1 - num2)
    q = flip(k)
    return num1 * k + num2 * q

    



print(get_max1(12, -2))
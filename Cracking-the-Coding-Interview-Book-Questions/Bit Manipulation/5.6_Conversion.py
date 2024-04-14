# Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
# EXAMPLE
# Input: 29 (or: 111101), 15 (or: 101111)
# Output: 2

def bitcount(n):
    count = 0
    while n > 0:
        count += 1
        n = n & (n-1)
    return count

def find_bit_count(num1, num2):
    x = num1 ^ num2
    # count the no. of set bits in a no.
    return bitcount(x)


print(find_bit_count(29, 15))
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def compute_sum_squares(num):
    total = 0
    while num != 0:
        remainder = num % 10
        total += remainder ** 2
        num = num // 10
    return total


def isHappy(n: int):
    
    seen = set()
    current = n
    while current != 1 and current not in seen:
        seen.add(current)
        current = compute_sum_squares(current)
    
    return current == 1



n = 19
print(isHappy(n))
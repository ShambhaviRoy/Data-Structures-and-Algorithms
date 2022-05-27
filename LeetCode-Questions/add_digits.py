# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# https://leetcode.com/problems/add-digits/

# Example: num = 38
# Output = 2
# 38 --> 3 + 8 = 11
# 11 --> 1 + 1 = 2 (ans) 


# Approach 1: Loop
def add_digits(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num = num // 10

        if num == 0 and ans > 9:
            num = ans 
            ans = 0

    return ans



# Approach 2:
# ans = 0 if num == 0
# ans = 9 if num = 9k
# ans = n mod 9 if num != 9k

# Time Complexity = O(1), Space Complexity = O(1)

def add_digits2(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


num = 38
print(add_digits(num))
print(add_digits2(num))
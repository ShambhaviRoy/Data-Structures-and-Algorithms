# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2

# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


# Approach:
# The minimum sum is possible by adding two 2-digit no.s --> split the no. into 2 digit parts 
# 2 larger digits in ones place, 2 smaller digits in tens place


def min_sum(num):
    num_digits = []
    
    # find all 4 digits of num
    while num > 0:
        num_digits.append(num % 10)
        num = num // 10

    num_digits.sort(reverse=True)

    # create the 2 digit no.s and return their sum
    # iterating over num_digits
    ans = 0
    position = 0
    even_iteration = True
    for i in range(4):
        ans += num_digits[i] * (10**position)
        if not even_iteration:
            position += 1
            even_iteration = True
        else:
            even_iteration = False
    return ans

    

num = 2932
print(min_sum(num))
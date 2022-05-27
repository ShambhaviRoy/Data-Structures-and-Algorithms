# Given an unsigned integer n, find the no. of 1 bits in it
# Input is a binary string of length 32

# https://leetcode.com/problems/number-of-1-bits/

# Using bitwise and (&) operation

def hamming_weight(n):
    ans = 0
    while n:
        n &= n-1
        ans += 1
    return ans


n = int(input())
print(hamming_weight(n))
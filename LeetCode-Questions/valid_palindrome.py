# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# https://leetcode.com/problems/valid-palindrome/


def check_palindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def valid_palindrome(s):
    alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"

    s = s.lower()
    s1 = ''.join([c for c in s if c in alphanumeric])
    return check_palindrome(s1)


s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
print(valid_palindrome(s1))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
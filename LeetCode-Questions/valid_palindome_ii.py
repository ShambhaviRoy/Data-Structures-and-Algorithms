# Given a string s, return true if the s can be palindrome after deleting at most one character from it

# https://leetcode.com/problems/valid-palindrome-ii/

# Examples:
# Input s = "aba", Output = true
# Input s = "abca", Output = true 
# Input s = "racecar", Output = true
# Input s = "papa", Output = false

# Approach: Use 2 pointers to traverse s, if characters at these pointers are not same, move these pointers 1 place and check whether the substring created is a palindrome or not. 
# To be a valid palindrome, s should be a palindrome when either substring is a palindrome.

# Time complexity = O(n^2)
# Space complexity = O(1)

def check_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome_ii(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return check_palindrome(s, start+1, end) or check_palindrome(s, start, end-1)
        else:
            start += 1
            end -= 1
    return True


s1 = "racecar"
s2 = "papa"
print(valid_palindrome_ii(s1))
print(valid_palindrome_ii(s2))
            
        
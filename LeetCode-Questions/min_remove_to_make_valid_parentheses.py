# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 
# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either '(' , ')', or lowercase English letter.

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/


# Solution 1: Using a stack to maintain order of valid parentheses and a set to keep track of indices having extra parentheses
# Time Complexity = O(n)
# Space Complexity = O(n)
def min_remove1(s):
    stack = []
    answer = ''
    to_remove = set()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    # add stack indices to remove
    if stack:
        to_remove = to_remove.union(set(stack))

    for i in range(len(s)):
        if i not in to_remove:
            answer += s[i]

    return answer


# Solution 2

def min_remove2(s):
    num_opens = 0
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if s[i] == '(':
            num_opens += 1
        elif s[i] == ')':
            if num_opens > 0:
                num_opens -= 1
            else:
                stack.pop()
            
    i = len(stack) - 1
    while i > 0 and num_opens > 0:
        if stack[i] == '(':
            stack[i] == ''
            num_opens -= 1
        i -= 1

    return ''.join(stack)

    
s1 = "lee(t(c)o)de)"
print(min_remove1(s1))
print(min_remove2(s1))

s2 = "a)b(c)d"
print(min_remove1(s2))
print(min_remove2(s2))

s3 = "))(("
print(min_remove1(s3))
print(min_remove2(s3))
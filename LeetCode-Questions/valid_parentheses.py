# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# https://leetcode.com/problems/valid-parentheses/description/


def valid_parentheses(s):
    # mapping closing and opening brackets
    bracket_map = {')':'(' , '}':'{', ']':'['}

    if(len(s) %2 != 0):
        return False
    
    stack = []

    for bracket in s:
        if bracket in bracket_map.values():
            stack.append(bracket)
        else:
            top = stack.pop() if stack else '0'
            if(top != bracket_map[bracket]):
                return False


    return stack == []



s1 = '({[]})'
print(valid_parentheses(s1))

s2 = '([{(}])'
print(valid_parentheses(s2))
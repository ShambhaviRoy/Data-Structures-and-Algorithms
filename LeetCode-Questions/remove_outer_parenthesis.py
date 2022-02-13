# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
 
# https://leetcode.com/problems/remove-outermost-parentheses/

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".


def removeOuterParentheses(s):
    
    stack = []
    dec = []
    # ans = ''
    decomposition = ''
    
    for bracket in s:
        decomposition += bracket
        if bracket == '(':
            stack.append(bracket)
        else:
            stack.pop()
        if len(stack) == 0:
            dec.append(decomposition[1:len(decomposition)-1])
            decomposition = ''

    # return ans
    return ''.join(dec)
                


if __name__ == '__main__':
    s = input()
    print(removeOuterParentheses(s))
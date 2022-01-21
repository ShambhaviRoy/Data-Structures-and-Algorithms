# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
# Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

# Examples: 
# s = 'abc' --> This is a valid string because frequencies are {'a':1, 'b':1, 'c': 1}.
# s = 'abcc' --> This is a valid string because we can remove one c and have 1 of each character in the remaining string.
# s = 'abccc' --> This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {'a':1, 'b':1, 'c': 2}.

# Constraints:
# 1 <= len(s) <= 10^5
# Each character in s is a lowercase ASCII alphabet


from collections import Counter

def isValid(s):
    string = Counter(s)     # string = {'char': its count}
    # print(string)
    
    string = Counter(string.values())   # string = {count: no. of chars in s with that count value}
    # print(string)
    
    # if s has only 1 char
    if len(string.keys())==1:
        return "YES"
    
    # if s has chars with 2 different count values
    elif len(string.values()) == 2:
        key1, key2 = string.keys()
        if string[key1] == 1 and (key1-1 == key2 or key1-1 == 0):
            return "YES"
        elif string[key2]==1 and (key2-1==key1 or key2-1==0):
            return "YES"
        else:
            return "NO"

    else:
        return "NO"



if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)
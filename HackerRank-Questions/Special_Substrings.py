# A string is said to be a special string if either of two conditions is met:
# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

# Constraints:
# 1 <= n <= 10^6

def substrCount(n, s):
    ans = 0
    for i in range(len(s)):
        ans += 1
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                if 2*j-i < len(s) and s[i:j] == s[j+1: 2*j-i+1]:    # if left part of the substring is equal to the right part
                    ans += 1
                    break
                else:
                    break
            else:
                ans += 1            
    return ans


if __name__ == '__main__':
    s = input()
    result = substrCount(len(s), s)
    print(result)
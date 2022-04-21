# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

def longest_substring(s):
    start = 0
    end = 0
    ans = 0
    li_dict = defaultdict(int)
    
    while end < len(s):
        if s[end] in li_dict:
            start = max(start, li_dict[s[end]]+1)
        li_dict[s[end]] = end
        ans = max(ans, end - start + 1)
        end += 1

    return ans



s = input()
print(longest_substring(s))


'''
s = 'abcabcbb', len(s) = 8
0 < 8,   li_dict = {a : 0},     ans = 1,    end = 1
1 < 8,  {a:0, b:1},     2,  2
2 < 8, {a:0, b:1, c:2}, 3,  3
3 < 8, start = max(0, 1) = 1, {a: 3, b: 1, c:2},    max(3, 3-1+1) = 3, end = 4
4 < 8, start = max(4, 5) = 5, {a:3, b:5, c:2},  max(3, 3-1+1) = 3, end = 5
...
'''


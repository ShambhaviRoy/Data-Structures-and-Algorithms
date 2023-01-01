# https://leetcode.com/problems/longest-duplicate-substring/description/

# Steps:
# 1. Iterate over s from 0th index
# 2. For each index, define a substring of length 1 initially
# 3. Check whether the substring exists in s: If yes, increment substring length (step) and repeat, else go to next index in s and repeat

# Time Complexity = O(n)

def longestDuplicateSubstring(s):
    ans = ""

    start = 0
    step = 1

    for start in range(len(s)):
        substring = s[start : start + step]
        remaining = s[start + 1 : ]
        while substring in remaining:
            ans = substring
            step += 1
            substring = s[start : start + step]

    return ans


s = "banana"
print(longestDuplicateSubstring(s))
# Longest Uniform Substring

# Given a string, find the longest substring with the same character 
# Return a list containing the starting index of the longest uniform substring and the length of this substring
# Example:
# Input = "aabbbbbCdAA", output = [2, 5]

def longest_uniform_substring(s):
    if len(s) == 0:
        return [-1, 0]

    start = 0
    substr_len = 1
    best_start = 0
    best_len = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            substr_len += 1
        else:
            if best_len < substr_len:
                best_len = substr_len
                best_start = start
            substr_len = 1
            start = i

    return [best_start, best_len]


s = "aabbbbbCdAA"
print(longest_uniform_substring(s))
        
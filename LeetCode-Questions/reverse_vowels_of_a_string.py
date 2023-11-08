# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

# Approach: Keep 2 pointers, one for the start of the string and one at the end, keep moving these pointers until both point to vowels and swap

# Time complexity = O(n)
# Space complexity = O(n)

def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    start = 0
    end = len(s) - 1
    s = list(s)
    
    while start < end:
        while start < end and s[start] not in vowels:
            # keep moving start pointer ahead till we find a vowel
            start += 1
        while start < end and s[end] not in vowels:
            # keep moving end pointer ahead till we find a vowel
            end -= 1
        s[start], s[end] = s[end], s[start] # swap
        start += 1
        end -= 1

    return ''.join(s)


s1 = 'hello'
s2 = 'leetcode'
print(reverse_vowels(s1))
print(reverse_vowels(s2))


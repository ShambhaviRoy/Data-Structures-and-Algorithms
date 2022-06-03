# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

# https://leetcode.com/problems/maximum-product-of-word-lengths/

# Example:
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".


# Approach: Bit Manipulation
# Create a binary mask for each word that represents each character in binary 
# If the bitwise and of 2 masks is 0, they have nothing in common

# Time Complexity = O(n^2)


def find_max_prod(words):
    ans = 0
    n = len(words)
    masks = [0]*n

    for i in range(n):
        for ch in words[i]:
            masks[i] |= 1 << (ord(ch) - ord('a'))
        for j in range(i):
            if masks[i] & masks[j] == 0:
                ans = max(ans, len(words[i])*len(words[j]))

    return ans


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(find_max_prod(words))
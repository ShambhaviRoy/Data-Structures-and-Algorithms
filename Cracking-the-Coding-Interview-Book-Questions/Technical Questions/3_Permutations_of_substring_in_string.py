# Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation.


# Approach:
# Sliding window, count the no. of characters in the window, if it matches substring, print position and move ahead till the end of the longer string

# Time complexity = O(len(b))
# Space complexity = O(len(s))

import collections


def permutations_of_substring(s, b):
    start = 0
    end = start + len(s)

    s_map = collections.Counter(s)

    while((start < end) & (end < len(b))):
        pos = start
        window = b[start : end]
        window_map = collections.Counter(window)
        if s_map == window_map:
            print(pos)
            start += len(s)
            end = start + len(s)
        else:
            start += 1
            end += 1





# Sample input
s = "abbc"
b = "cbabadebbabbebabaabcebabe"

permutations_of_substring(s, b)


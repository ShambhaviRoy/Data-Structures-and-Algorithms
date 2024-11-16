# 408. Valid Word Abbreviation
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

# The following are not valid abbreviations: 
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)

# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
# A substring is a contiguous non-empty sequence of characters within a string.

# https://leetcode.com/problems/valid-word-abbreviation/description/

def valid_word_abbreviation(word, abbr):
    word_ptr, abbr_ptr = 0, 0
    n = len(word)
    k = len(abbr)

    while word_ptr < n and abbr_ptr < k:
        if word[word_ptr] != abbr[abbr_ptr] and not abbr[abbr_ptr].isdigit():
            return False
        elif word[word_ptr] != abbr[abbr_ptr] and abbr[abbr_ptr].isdigit():
            # get number
            if int(abbr[abbr_ptr]) == 0: # leading 0
                return False
            num = 0
            while abbr_ptr < k and abbr[abbr_ptr].isdigit():
                num = num * 10 + int(abbr[abbr_ptr])
                abbr_ptr += 1
            word_ptr += num
        else:
            word_ptr += 1
            abbr_ptr += 1

    return word_ptr == n and abbr_ptr == k



print(valid_word_abbreviation("substitution", "s10n"))
print(valid_word_abbreviation("substitution", "s55n"))
print(valid_word_abbreviation("substitution", "s0ubstitution"))


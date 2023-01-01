# https://leetcode.com/problems/word-pattern/

# Bijection: Every element of the pattern matches with exactly 1 element of s and vice versa

def wordPattern(s, pattern):
    s_split = s.split()

    if(len(pattern) != len(s_split)):
        return False
    
    # mapping a letter in pattern with a word in s
    pattern_dict = {}
    for ch, word in zip(pattern, s_split):
        if ch not in pattern_dict:
            pattern_dict[ch] = word
        else:
            if pattern_dict[ch] != word:
                return False

    # Every key (letter in pattern_dict) should have unique corresponding value (word)
    if len(pattern_dict) != len(set(pattern_dict.values())):
        return False
    else:
        return True


pattern = "abba"
s = "dog cat dog cat"
print(wordPattern(s, pattern))

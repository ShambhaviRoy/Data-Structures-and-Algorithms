# An anagram is when two strings can be written using the same letters.
# "rail safety" --> "fairy tales"

s1 = "rail safety"
s2 = "fairy tales"

# Approach 1:
# Time Complexity = O(nlogn)
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
print(sorted(s1) == sorted(s2))

# Approach 2:
# Time Complexity = O(n)
def is_anagram(s1, s2):
    letter_dict = dict()

    if len(s1) != len(s2):
        return False

    # Storing letters of s1 and its count in letter_dict
    for letter in s1:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    # Checking occurrence of each letter in s2 with letter_dict
    # Reducing count for each letter found --> verifying
    for letter in s2:
        if letter in letter_dict:
            letter_dict[letter] -= 1

    # If each value is 0, s1 and s2 have the same letters equal number of times --> anagrams
    for letter in letter_dict:
        if letter_dict[letter] != 0:
            return False

    return True 

print(is_anagram(s1, s2))
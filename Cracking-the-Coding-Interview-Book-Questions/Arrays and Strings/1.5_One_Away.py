#There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

# Time complexity = O(n), Space complexity = O(n), n = len(longer string)
def oneEditAway(str1, str2):
    # Length check
    if len(str1) - len(str2) > 1:
        return False

    # Get shorter and longer
    s1 = str1 if len(str1) < len(str2) else str2
    s2 = str2 if len(str2) < len(str1) else str1

    index1 = 0
    index2 = 0
    foundDifference = False

    while (index2 < len(s2)) and (index1 < len(s1)):
        if s2[index2] != s1[index1]:
            # Ensure that this is the first difference found
            if foundDifference:
                return False
            else:
                foundDifference = True

            # On replace, move shorter pointer
            if len(s1) == len(s2):
                index1 += 1
        
        # If matching, move shorter pointer
        else:
            index1 += 1

        # Always move longer pointer
        index2 += 1

    return True 


# Approach 2: Using dict
# Store the counts of characters of longer string in a dict
# Iterate over shorter string, drop counts of char from dict, but if only 1 char found, drop it from dict
# Check if the dict has only 1 key
# Time complexity = O(n), Space Complexity = O(n), n = len(longer string)
import collections

def one_edit_away2(str1, str2):
    longer = str1 if len(str1) > len(str2) else str2
    shorter = str1 if len(str1) < len(str2) else str1

    if len(longer) - len(shorter) > 1:
        return False
    
    char_dict = collections.Counter(longer)
    for char in shorter:
        if char in char_dict:
            count = char_dict[char]
            if count > 1:
                char_dict[char] -= 1
            else:
                del char_dict[char]

    return len(char_dict.keys()) <= 1


str1 = "pale"
str2 = "plex"
print(oneEditAway(str1, str2))
print(one_edit_away2(str1, str2))

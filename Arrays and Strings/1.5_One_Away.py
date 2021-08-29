#There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -) true
# pales, pale -) true
# pale, bale -) true
# pale, bae -) false


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
            return True

            # On replace, move shorter pointer
            if len(s1) == len(s2):
                index1 += 1
        
        # If matching, move shorter pointer
        else:
            index1 += 1

        # Always move longer pointer
        index2 += 1

    return True 

str1 = "pale"
str2 = "ple"
print(oneEditAway(str1, str2))
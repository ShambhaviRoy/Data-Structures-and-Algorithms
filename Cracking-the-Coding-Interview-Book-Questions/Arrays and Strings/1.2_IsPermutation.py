# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

# Approach 1: Using dict
# Add elements of first string in a dict, iterate through other string and for each character, drop its count by 1 in the dict
# Time Complexity = O(n), Space Complexity = O(n)
def ispermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()
    sdict = dict()

    #traverse str1 and update its characters and their count in sdict
    for letter in str1:
        if letter in sdict:
            sdict[letter] += 1
        else:
            sdict[letter] = 1

    #traverse str2 to remove occurrences in sdict
    for letter in str2:
        if letter in sdict:
            sdict[letter] -= 1
            if sdict[letter] == 0:
                sdict.pop(letter)

    # check sdict
    return sdict == {}


# Approach 2: Without using additional data structure
# Iterate over a string and if it's char is found in 1st string, replace with ""
# Finally check whether string 1 is reduced to ""
# Time Complexity = O(n), Space Complexity = O(1)
def is_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    for char in str2:
        str1 = str1.replace(char, "")
    return str1 == ""



str1 = "train"
str2 = "trained"
print(ispermutation(str1, str2))
print(is_permutation2(str1, str2))


str3 = "train"
str4 = "ainrt"
print(ispermutation(str3, str4))
print(is_permutation2(str3, str4))


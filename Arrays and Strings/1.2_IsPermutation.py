# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def ispermutation(str1, str2):
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

    # check values in sdict
    for char, count in sdict.items():
        if count != 0:
            return False

    return True


str1 = "train"
str2 = "trained"
print(ispermutation(str1, str2))

str3 = "train"
str4 = "ainrt"
print(ispermutation(str1, str2))

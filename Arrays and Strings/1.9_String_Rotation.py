# Assume you have a method isSubst ring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(str1, str2):
    letters = dict()

    for ch in str1:
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1

    for ch in str2:
        if ch in letters:
            letters[ch] -= 1
        
    #for ch, count in letters.items():
    #    if count != 0:
    #        return False
    #return True

    return all(value == 0 for value in letters.values())

def stringRotation(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == 0 or len(s2) == 0:
        return False
    elif (len(s1) != len(s2)):
        return False
    else:
        return isSubstring(s1, s2)

s1 = "waterbottle"
s2 = "erbottlewat"
print(stringRotation(s1, s2))
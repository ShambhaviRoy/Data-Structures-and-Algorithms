# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(s1, s2):
    longer = s1 if len(s1) >= len(s2) else s2
    shorter = s2  if len(s1) >= len(s2) else s1
    i = 0
    while i < len(longer):
        j = 0
        while i < len(longer) and j < len(shorter) and longer[i] == shorter[j]:
            i += 1
            j += 1
        if j == len(shorter):
            return True
        i += 1
    return False

def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1 = s1.lower()
    s2 = s2.lower()
    return isSubstring(s1 + s1, s2)
    

s1 = "waterbottle"
s2 = "erbottlewat"
print(stringRotation(s1, s2))
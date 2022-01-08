#Is Unique: Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?

#Approach 1: Using Python dict
def isUnique1(str):
    sdict = dict()
    for ch in str:
        #increment char count
        if ch in sdict:
            sdict[ch] += 1
        else:
            sdict[ch] = 1
        #traverse the dict to check count for each letter
        for char, count in sdict.items():
            if count > 1:
                return False
        return True

#Approach 2: Without data structure
def isUnique2(str):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    str = str.lower()
    for letter in str:
        if letter in alpha:
            alpha = alpha.replace(letter, "")
        else:
            return False
    return True

str1 = "shambhavi"
str2 = "Shambhavi@11"
print(isUnique1(str1))
print(isUnique2(str2))

#Is Unique: Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?

#Approach 1: Using Python dict
# Time Complexity = O(n), Space Complexity = O(n)
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


# Approach 2: Using set
# Time Complexity = O(n), Space Complexity = O(n)
def isUnique2(str):
    return len(str) == len(set(str))


#Approach 3: Without data structure
# Time Complexity = O(n), Space Complexity = O(n)
def isUnique3(str):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    str = str.lower()
    for letter in str:
        if letter in alpha:
            alpha = alpha.replace(letter, "")
        else:
            return False
    return True


# Approach 4: Without additional data structure
# Sort the string and traverse through it, if previous character is same as current, it does not have all unique characters
# Time Complexity = O(n log n), Space Complexity = O(n)
def isUnique4(str):
    str = ''.join(sorted(str))
    for i in range(len(str)-1):
        if(str[i-1] == str[i]):
            return False
    return True


# Approach 5: 2 pointer
# Time Complexity = O(n^2), Space Complexity = O(1)
def isUnique5(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True



str1 = "shambhavi"
print(isUnique1(str1))
print(isUnique2(str1))
print(isUnique3(str1))
print(isUnique4(str1))
print(isUnique5("abcdef"))

# Write a function that returns whether two words are exactly "one edit" away using the following signature:
# bool OneEditApart(string s1, string s2);
# An edit is:
# Inserting one character anywhere in the word (including at the beginning and end)
# Removing one character
# Replacing one character

def OneEditApart(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i, j = 0, 0
    saw_difference = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if saw_difference:
                return False
            saw_difference = True
            if len(s1) > len(s2):
                i -= 1
        else:
            i += 1
        j += 1

    return saw_difference or len(s1) != len(s2)
            

print(OneEditApart('cat', 'dog'))
print(OneEditApart('cat', 'cats'))
print(OneEditApart('cats', 'cat'))
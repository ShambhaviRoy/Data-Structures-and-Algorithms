# Check if 2 strings are permutations of each other

# Approach 1: Sorting
# Time Complexity = O(nlogn), Space Complexity = O(1)
def check_perm1(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return (sorted(s1) == sorted(s2))


# Approach 2: Maintain dict
def check_perm2(s1, s2):
    if len(s1) != len(s2):
        return False

    letter_dict = dict()
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # populate letter_dict with letters in s1 and their count
    for letter in s1:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    # check with s2
    for letter in s2:
        if letter in letter_dict:
            letter_dict[letter] -= 1

    return all(value == 0 for value in letter_dict.values())

    
    

s1 = "Google"
s2 = "ooGgle"
print(check_perm1(s1, s2))
print(check_perm2(s1, s2))
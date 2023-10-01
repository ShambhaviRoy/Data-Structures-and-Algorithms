# Example: Design an algorithm to print all permutations of a string. For simplicity, assume all characters
# are unique.

# Approach
# Take the first letter and place the 2nd letter
# Then place the 3rd letter around the first 2, and keep going --> recursion


def permutations(s):
    if len(s) == 1:
        return s
        
    permutations_list = []

    for ch in s:
        for a in permutations(s.replace(ch, "", 1)): 
            permutations_list.append(ch + a)
    
    return set(permutations_list)


def create_permutations(s, start = 0):    
    if start == len(s) - 1:
        print("".join(s))
    else:
        for i in range(start, len(s)):
            # swap current element with last element
            s[start], s[i] = s[i], s[start]
            # recursively create permutations on the rest of the string
            create_permutations(s, start + 1)
            # back tracking
            s[start], s[i] = s[i], s[start]



s = "abc"
print(permutations(s))

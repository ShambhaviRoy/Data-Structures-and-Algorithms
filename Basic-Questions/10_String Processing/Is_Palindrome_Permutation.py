# Palindrome --> A string which spells forwards and backwards.
# Permutation --> A combination of letters.
# Example: "taco cat"
# Observations:
# A string with even length has all characters with even count.
# A string with odd length has only one character in odd count.

def is_palin_perm(s):
    length = len(s)
    letter_dict = dict()    # to store each letter and count

    s = s.replace(" ", "").lower()

    for letter in s:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    odd_count = 0
    for key, value in letter_dict.items():
        if value % 2 != 0 and odd_count == 0:
            odd_count = 1
        elif value % 2 != 0 and odd_count >= 1:
            odd_count += 1
    
    if odd_count > 1:
        return False
    else:
        return True



s1 = "taco cat"
s2 = "shambhavi"
print(is_palin_perm(s1))
print(is_palin_perm(s2))
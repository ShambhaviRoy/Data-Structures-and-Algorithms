# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)


# Approach 1: Scan through the string to keep counts of each character, at most 2 character can have odd count
# Time complexity = O(n)
# Space complexity = O(n)

def palinperm(input_str):
    sdict = dict()

    for char in input_str:
        if char in sdict:
            sdict[char] += 1
        else:
            sdict[char] = 1

    count_odd = 0
    for char, count in sdict.items():
        if count %2 != 0:
            count_odd += 1

    return (count_odd <= 2)


# Approach 2: We do not need to know the count of each character, just need to know whether it is even/odd
# Assume that the input string has 26 letters (all lower case), keep a bit vector to track whether the count of character at that position is odd/even (0 means even count)
# then check whether only 1 bit in this vector is set (1) --> subtract 1 from the bit vector and AND it with the original bit vector

# Example:
# str = "racecar"
# bit_vector = [0, 0, 0, 0, 0, ...1,  ...0] --> written as list to visualize easily
#               a, b, c, d, e, ...r,  ...z

# Time complexity = O(n)
# Space complexity = O(1)

def toggle_bit(bit_vector, position):
    if position < 0:
        return bit_vector
    mask = 1 << position
    bit_vector = bit_vector ^ mask
    return bit_vector


def bit_vector_palinperm(input_str):
    bit_vector = 0
    input_str.lower()

    for char in input_str:
        # find position of char in alphabet
        position = ord(char) - ord('a')
        # toggle bit at that position
        bit_vector = toggle_bit(bit_vector, position)

    # check
    return (bit_vector & bit_vector-1) == 0


print(palinperm("taco cat"))
print(bit_vector_palinperm("taco cat"))
print(bit_vector_palinperm("shambhavi"))


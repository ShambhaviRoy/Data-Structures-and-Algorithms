# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

def palinperm(input_str):
    sdict = dict()
    if len(input_str) % 2 == 0:
        is_odd = True
    else:
        is_odd = False

    for char in input_str:
        if char in sdict:
            sdict[char] += 1
        else:
            sdict[char] = 1

    for char, count in sdict.items():
        if count %2 == 0:
            if is_odd:
                return False
        

    return True

print(palinperm("tacocat"))
print(palinperm("shambhavi"))


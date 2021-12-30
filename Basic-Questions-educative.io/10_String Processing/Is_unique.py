def normalize_str(input_str):
    return input_str.replace(" ", "").lower()

# Approach 1: Maintaining a dictionary
# Time Complexity = O(n)
def is_unique_1(input_str):
  letter_dict = dict()
  for letter in input_str:
    if letter in letter_dict:
      letter_dict[letter] += 1
    else:
      letter_dict[letter] = 1
  return all(values == 1 for values in letter_dict.values())


# Approach 2: Set
# Python's set() method converts a string to a set removing all duplicates
# If the string is unique, its length will be equal to its set form
def is_unique_2(input_str):
    return (len(set(input_str)) == len(input_str))


# Approach 3: 
def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in input_str:
        if letter in alpha:
            alpha = alpha.replace(letter, "")
        else:
            return False
    return True


s1 = "aBcDeFgHi"
s2 = "Shambhavi"
print(is_unique_1(normalize_str(s1)))
print(is_unique_1(normalize_str(s2)))
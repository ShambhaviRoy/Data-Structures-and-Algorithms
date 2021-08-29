# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# helper function
def idx(char, str):
    return str.index(char)

def URLify(input_str, length):
    # truncate to length
    str = input_str[:length]

    for char in str:
        if char == ' ':
            cidx = idx(char, str)
            str = str[: cidx] + '%20' + str[cidx+1 :]
        
    return str 

input_str1 = "Mr John Smith      "
input_str2 = "Shambhavi Roy        "
print(URLify(input_str1, 13))
print(URLify(input_str2, 13))

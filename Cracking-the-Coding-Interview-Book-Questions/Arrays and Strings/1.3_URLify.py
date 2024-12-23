# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# Approach 1: Scan through the string for spaces, if found, create a new copy of the string replacing spaces with '%20'
# Time complexity = O(n^2)
# Space complexity = O(n)

def URLify(input_str, length):
    # truncate to length
    str = input_str[:length]

    for i, char in enumerate(str):
        if char == ' ':
            str = str[: i] + '%20' + str[i+1 :]
            print(str)
        
    return str 


# Approach 2: Convert the string to a list, traverse through the list to replace the space with '%20' and join it in the end
# Time complexity = O(n)
# Space complexity = O(n)

def URLify2(input_str, length):
    str_list = list(input_str[:length])
    for i in range(length):
        if str_list[i] == ' ':
            str_list[i] = '%20'
    return ''.join(str_list)


# Approach 3: Convert the string to a list, split string on space and join the parts with '%20'
# Time complexity = O(n)
# Space complexity = O(n)

def URLify3(input_str, length):
    str = input_str[:length]
    return str.replace(' ', '%20')


input_str1 = "Mr John Smith      "
print(URLify2(input_str1, 13))
print(URLify3(input_str1, 13))

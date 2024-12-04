# Pattern Matching: You are given two strings, pattern and value. The pattern string consists of
# just the letters a and b, describing a pattern within a string. For example, the string "catcatgocatgo"
# matches the pattern "aabab" (where "cat" is 'a' and "go" is 'b'). It also matches patterns like a, ab, and b.
# Write a method to determine if value matches pattern.


# check if substring of value and check whether it matches pattern

def does_match(pattern : str, value : str):
    if(len(pattern) == 0):
        return len(value) == 0
    
    main_char = pattern[0]
    alt_char = 'b' if main_char == 'a' else 'a'
    size = len(value)

    count_of_main = pattern.count(main_char)
    count_of_alt = len(pattern) - count_of_main
    first_alt = pattern.index(alt_char)
    max_main_size = size // count_of_main

    for main_size in range(max_main_size):
        remaining_length = size - main_size * count_of_main
        if(count_of_alt == 0 or remaining_length % count_of_alt == 0):
            alt_index = first_alt * main_size
            alt_size = 0 if count_of_alt == 0 else remaining_length // count_of_alt
            if(matches(pattern, value, main_size, alt_size, alt_index)):
                return True
            
    return False

# iterate through pattern and value and checks if it is the main string or alternate string
# Check if the next characters in value match the original set of characters (main or alternate)
def matches(pattern, value, main_size, alt_size, alt_index):
    string_index = main_size
    for i in range(1, len(pattern) - 1):
        size = main_size if pattern[i] == pattern[0] else alt_size
        offset = 0 if pattern[i] == pattern[0] else alt_index
        if not is_equal(value, offset, string_index, size):
            return False
        string_index += 1
    return True


# check if 2 substrings are equal, beginning at offset and continuing upto size
def is_equal(string, offset1, offset2, size):
    for i in range(size):
        if string[offset1 + i] != string[offset2 + i]:
            return False
    return True



print(does_match("aabab", "catcatgocatgo"))

# Count the occurrence of a substring in a string using recursion
# Examples: 
# Input: string = 'geeksforgeeks', substring = 'geeks' --> Output = 2
# Input: string = 'hikakashi', substring = 'geeks' --> Output = 2


def count_substring(str, substr):
    len_str = len(str)
    len_substr = len(substr)

    # base case
    if len_str == 0 or len_str < len_substr:
        return 0
    
    if str[0:len_substr] == substr:
        return 1 + count_substring(str[len_substr-1:], substr)
    
    return count_substring(str[len_substr-1:], substr)

    
if __name__ == '__main__':
    str = 'geeksforgeeks'
    substr = 'geeks'
    print(count_substring(str, substr))

    str2 = 'hikakashi'
    substr2 = 'hi'
    print(count_substring(str2, substr2))

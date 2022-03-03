# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# https://leetcode.com/problems/longest-common-prefix/


def longest_prefix(st):
    ans = ''
    prefix = st[0]

    for string in st[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break
    ans = prefix
    return ans


if __name__ == '__main__':
    print('Enter number of strings in list:')
    n = int(input())
    st = []

    for _ in range(n):
        st.append(input())

    print(longest_prefix(st))
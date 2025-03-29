# 249. Group Shifted Strings
# Perform the following shift operations on a string:

# Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
# Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
# We can keep shifting the string in both directions to form an endless shifting sequence.

# For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
# You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

# https://leetcode.com/problems/group-shifted-strings/description/


# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Approach: Traverse through each string and check unicode difference between successive characters, group strings with same successive character differences
# Time Complexity = O(n * k), n = no. of strings, k = length of longest string
# Space Complexity = O(n)

from collections import defaultdict

def group_shifted_strings(strings):
    table = defaultdict(list)
    for s in strings:
        key = ''
        for i in range(len(s) - 1):
            diff = ord(s[i + 1]) - ord(s[i])
            if diff < 0:
                diff += 26
            key += str(diff)
        table[key].append(s)
    return list(table.values())


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(group_shifted_strings(strings))
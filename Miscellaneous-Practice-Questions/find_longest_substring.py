# Find the length of the longest substring of a given string s that has unique characters. No need to find the substrings of the s.
# Example: s = 'cabbage'
# Output = 4 --> substring is 'bage'

# 2 pointer approach
# Time Complexity: O(n), Space Complexity = O(n)
def find_length(s):
    ans = 0
    start = end = 0

    last_index = {} # dict to store last index of each character

    while end < len(s):
        if s[end] in last_index:    # if character is repeated, move start pointer to the last index o
            start = max(start, end+1)
        ans = max(ans, end-start+1) # update ans
        last_index[s[end]] = end    # update last index of the character at end position
        end += 1

    return ans



if __name__ == '__main__':
    s = input()
    print(find_length(s))
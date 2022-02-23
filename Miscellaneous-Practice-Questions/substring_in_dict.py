# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be separated into a space-separated sequence of one or more words in the dictionary.

# Time Complexity = O(n^2), Space Complexity = O(n)

def space_separated(s, wordDict):
    n = len(s)
    can_separate = [False for i in range(n+1)]
    can_separate[0] = True

    for forward in range(1, n+1):
        for backward in range(forward-1, -1, -1):
            if can_separate[forward] == True:
                break
            if can_separate[backward]:
                # check if a new substring is formed from this point
                if s[backward:forward] in wordDict:
                    can_separate[forward] = True

    return can_separate[n]


"""
Dry run:
s = 'facebook'
wordDict = ['face', 'book', 'facebook']

Initially:
n = 8
can_separate = [True, False, False, False, False, False, False, False]

forward = 1, 
backward = 0 --> s[0:1] = 'f' 

forward = 2
backward = 1 --> 
backward = 0 --> s[0:2] = 'fa'

forward = 3
backward = 2 -->
backward = 1 --> 
backward = 0 --> s[0:3] = 'fac'

forward = 4
backward = 3
backward = 2
backward = 1
backward = 0 --> s[0:4] = 'face' in wordDict --> can_separate[4] = True
So,
can_separate = [True, False, False, False, True, False, False, False]


forward = 5
backward = 4 --> s[4:5] = 'e'
backward = 3
backward = 2
backward = 1
backward = 0 --> s[0:5] = 'faceb' not in wordDict

forward = 6
backward = 5 --> s[5:6] = 'o'
backward = 4 --> s[4:6] = 'bo'
backward = 3
backward = 2
backward = 1
backward = 0 --> s[0:6] = 'facebo' not in wordDict

"""

# print the space separated words
def word_split(s, wordDict):
    n = len(s)
    solutions = {}
    solutions[n] = ['']

    def solve(ind):
        if ind not in solutions:
            solutions[ind] = [s[ind:j] + (tail and (' ' and tail)) 
                                for j in range(ind, n+1) 
                                if s[ind:j] in wordDict
                                for tail in solve(j)]
        return solutions[ind]
    solve(0)
    return solutions[0]


s = 'facebook'
wordDict = ['face', 'book', 'facebouk', 'facebook', 'bo', 'ok'] 
print(space_separated(s, wordDict))
print(word_split(s, wordDict))
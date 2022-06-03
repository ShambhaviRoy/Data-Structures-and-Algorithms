# Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

# Examples: 
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4


# Approach: Dynamic Programming
# Use a table (dp) to store the value of LCS 
# dp[m][n] stores the value of LCS(X[0:m], Y[0:n])
# Time Complexity = O(mn), Space Complexity = O(mn)


def find_LCS(X, Y, dp):
    m, n = len(X), len(Y)

    if m == 0 or n == 0:
        return 0

    if X[m-1] == Y[n-1]:
        dp[m][n] = 1 + find_LCS(X[:m-1], Y[:n-1], dp)
    else:
        dp[m][n] = max(find_LCS(X[:m-1], Y[:n], dp), 
                        find_LCS(X[:m], Y[:n-1], dp))

    return dp[m][n]


X = input()
Y = input()

dp = [[-1]*(len(Y)+1)]*(len(X)+1)
print(find_LCS(X, Y, dp))


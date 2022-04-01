# For any 2 given strings X and Y, find their longest common subsequence.

# Dynamic Programming
# dp[i][j] represents the length of longest common subsequence of X[0:i] and Y[0:j]
# dp[i][j] = dp[i-1][j-1] + 1 if X[i] == Y[j]
#          = max(dp[i][j-1], dp[i-1][j]) otherwise
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    i, j = 0, 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m][n]


# Recursive solution without using dp matrix 
def LCS_recursive(X, Y):
    if X == Y:
        return len(X)

    if len(X) == 0 or len(Y) == 0:
        return 0

    if X[0] == Y[0]:
        return 1 + LCS_recursive(X[1:], Y[1:])
    else:
        return max(LCS_recursive(X, Y[1:]), LCS_recursive(X[1:], Y))




if __name__ == '__main__':
    X = input()
    Y = input()

    print(LCS(X, Y))
    print(LCS_recursive(X, Y))
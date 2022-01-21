# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
# Example
# s1 = 'ABCD', s2 = 'ABDC'
# These strings have two children with maximum length 3, 'ABC' and 'ABD'. They can be formed by eliminating either the D or C from both strings. Return 3.



def commonChild(s1, s2):
    # Write your code here
    # n = len(s1)
    
    # dp = [[0]*(n+1) for _ in range(n+1)]
    
    # for r in range(1, n+1):
    #     for c in range(1, n+1):
    #         if s1[r-1] == s2[c-1]:
    #             dp[r][c] = dp[r-1][c-1] + 1
    #         else:
    #             dp[r][c] = max(dp[r-1][c], dp[r][c-1])
                
    # # print(dp)
    
    # return dp[-1][-1]

    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    if s1 == s2:
        return len(s1)
    
    if s1[-1] == s2[-1]:
        return 1 + commonChild(s1[:len(s1)-1], s2[:len(s2)-1])
    else:
        return max(commonChild(s1, s2[:len(s2)-1]), commonChild(s1[:len(s1)-1], s2))


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = commonChild(s1, s2)
    print(result)
# Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  
# Insert
# Remove
# Replace
# All of the above operations are of equal cost. 

# Example: str1 = "geek", str2 = "gesek"
# Output:  1


# Approach 1: Naive Recursion
# Time Complexity = O(3^m)
def find_edit_distance_recursive(str1, str2):
    m, n = len(str1), len(str2)
    if m == 0: 
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return find_edit_distance_recursive(str1[:m-1], str2[:n-1])
    else:
        return 1 + min(find_edit_distance_recursive(str1[:m], str2[:n-1]),  # Insert
                        find_edit_distance_recursive(str1[:m-1], str2[:n]), # Remove
                        find_edit_distance_recursive(str1[:m-1], str2[:n-1]))   # Replace



# Approach: Dynamic Programming
# Using a dp matrix to store
# Time Complexity = O(mn) --> m = len(str1), n = len(str2)

def find_edit_distance(str1, str2, dp):
    m, n = len(str1), len(str2)
    
    if m == 0:
        return n
    if n == 0:
        return m

    if dp[m][n] != -1:
        return dp[m][n]

    if str1[m-1] == str2[n-1]:
        if dp[m-1][n-1] == -1:
            dp[m][n] = find_edit_distance(str1[:m-1], str2[:n-1], dp)
            return dp[m][n]
        else:
            dp[m][n] = dp[m-1][n-1]
            return dp[m][n]

    else:
        if dp[m-1][n] != -1:
            m1 = dp[m-1][n]
        else:
            m1 = find_edit_distance(str1[:m-1], str2, dp)

        if dp[m][n-1] != -1:
            m2 = dp[m][n-1]
        else:
            m2 = find_edit_distance(str1, str2[:n-1], dp)

        if dp[m-1][n-1] != -1:
            m3 = dp[m-1][n-1]
        else:
            m3 = find_edit_distance(str1[:m-1], str2[:n-1], dp)
        dp[m][n] = 1 + min(m1, m2, m3)
        return dp[m][n]

    

    



str1 = 'sunday'
str2 = 'saturday'

print(find_edit_distance_recursive(str1, str2))

dp = [[-1]*(1+len(str2))]*(1+len(str1))
print(find_edit_distance(str1, str2, dp))
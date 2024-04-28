# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

# Approach 1: Recursive
# Time complexity = O(3^n), Space complexity = O(1)
def count_ways(n):
    if(n < 0):
        return 0
    if n == 0:
        return 1
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


# Approach 2: Memoization
# Save the repeated computations in an array, access them when needed later
# Time complexity = O(n), Space complexity = O(n)

def count_ways2(n):
    memo = [-1] * n
    return count_ways2_helper(n, memo)

def count_ways2_helper(n, memo):
    if n < 0: return 0
    if n == 0: return 1
    if memo[n] > -1: 
        return memo[n]
    else:
        memo[n] = count_ways2_helper(n-1, memo) + count_ways2_helper(n-2, memo) + count_ways2_helper(n-3, memo)
        return memo[n]




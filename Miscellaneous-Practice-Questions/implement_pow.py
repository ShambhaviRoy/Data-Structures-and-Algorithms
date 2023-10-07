# Implement the pow function: pow(x, n) = x**n

# Approach: Using recursion (base case and build)
# Optimization: If n is even, we can split the operation as pow(x, n) = pow(x, n/2) * pow(x, n/2)

# Time complexity = O(log n)
# Space complexity = O(n) --> size of call stack

def pow(x, n):
    if n == 0: return 1
    if n == 1: return x
    else:
        if(n > 1) and (n % 2 == 0):
            t = pow(x, n/2)
            return t*t
        else:
            return x * pow(x, n-1)
    

print(pow(9, 5))
print(pow(9, 6))

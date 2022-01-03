# Calculate x^n using recursion
# Conditions:
#  x^n = (x^(n/2) * (x^(n/2), n = even
#      = x * (x^(n-1), n = odd
#      = 1, n=0

def pow(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        y = pow(x, n/2)   
        return (y*y)
    else:
        return (x * pow(x, n-1))


if __name__ == "__main__":
    print(pow(2, 5))
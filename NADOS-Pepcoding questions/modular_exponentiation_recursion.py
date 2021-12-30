# Calculate x^n modulo M using recursion
# Conditions:
#  x^n % M = [(x^(n/2) % M) * (x^(n/2) % M)] % M, n = even
#           = [(x % M) * (x^(n-1) % M)] % M, n = odd
#           = 1, n=0

def mod(x, n, M):
    if n == 0:
        return 1
    if n % 2 == 0:
        y = mod(x, n/2, M)   
        return (y*y) % M
    else:
        return ((x % M) * mod(x, n-1, M))% M


if __name__ == "__main__":
    print(mod(2, 5, 7))
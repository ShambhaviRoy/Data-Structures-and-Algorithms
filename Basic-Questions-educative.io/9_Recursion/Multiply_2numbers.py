def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    # base case: if y is 0
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(recursive_multiply(2, 3))

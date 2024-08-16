# https://leetcode.com/problems/powx-n/description/

from collections import defaultdict

def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return x

    if n % 2 == 0:
        exp = myPow(x, n/2)
        return exp * exp
    else:
        if n > 0:
            return x * myPow(x, n - 1)
        else:
            return (1/x) * myPow(x, n + 1)
    

print(myPow(x = 2.00000, n = 10))
print(myPow(x = 2.10000, n = 3))
print(myPow(x = 2.00000, n = -2))


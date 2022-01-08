# You are given an array and you need to find number of tripets of indices i, j, k such that the elements at those indices are in geometric progression for a given common ratio r and i < j <k.
# Example
# arr = [1, 4, 16, 64], r = 4
# There are [1, 4, 16] and [4, 16, 64] at indices (0, 1, 2) and (1, 2, 3). Return 2.

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    ans = 0
    d1 = defaultdict(int)   # stores counts of each element in arr
    d2 = defaultdict(int)   # stores smaller elements which are in triplets

    for i in reversed(arr):
        if i*r in d2:
            ans += d2[i*r]
        if i*r in d1:
            d2[i] += d1[i*r]

        d1[i] += 1
        print(d1, d2, ans)
    return ans

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)

    
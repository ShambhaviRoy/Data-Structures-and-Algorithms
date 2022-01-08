# You are given q queries. Each query is of the form two integers described below:
# 1 x : Insert x in your data structure.
# 2 y : Delete one occurence of y from your data structure, if present.
# 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    data = defaultdict(int) # to store elements and their counts
    ans = []
    for i, el in queries:
        # i = 1 --> insert el in data
        if i == 1:
            if el not in data:
                data[el] = 1
            else:
                data[el] += 1
                
        # i = 2 --> delete one occurrence of el if present
        elif i == 2:
            if el in data.keys() and data[el] >= 1:
                data[el] -= 1
                
            
        # i = 3 -> check if element is present with freq=el, print 1
        else:
            ans.append(1 if el in set(data.values()) else 0)

    return ans

if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

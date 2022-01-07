# Given a  2D Array, arr:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in arr is a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
# 
# Constraints:
# -9 <= arr[i][j] <= 9
# 0 <= i, j <= 5


#!/bin/python3

import math
import os
import random
import re
import sys

def calc_sum(row, col):
    # calculating hourglass sum step by step
    add = 0
    add += arr[row][col] + arr[row][col+1] + arr[row][col+2]
    add += arr[row+1][col+1]
    add += arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
    return add

def hourglassSum(arr):
    hourglass = []
    for row in range(4):
        for col in range(4):
            hourglass.append(calc_sum(row, col))
            
    return max(hourglass)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

 
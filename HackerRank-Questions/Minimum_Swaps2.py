# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.


#!/bin/python3

import math
import os
import random
import re
import sys



def minimumSwaps(arr):
    swaps = 0
    min = None
    for i in arr:
        if min is None or min > i:
            min = i
    #defined a min, which is at 0, let's make sure it's at i=0
    min_i = arr.index(min)
    if min_i != 0:
        arr[0], arr[min_i] = arr[min_i], arr[0]
        swaps += 1
    
    #because the minimum is at 0 and they are all consecutive, it's basically an offset
    offset = arr[0]
    
    #initializing a dict copy that keeps track of the locations for quick find and swap
    index_dict = {v: i for i, v in enumerate(arr)}
    #starting at 1, 0 is already placed
    i = 0
    while i < len(arr) - 1:
        i += 1
        if not proper_place(arr, i, offset):
            try:
                val = arr[i]
                #testing for perfect swap
                if arr[val - offset - 1] == i:
                    arr[i], arr[val - offset] = arr[val - offset], arr[i]
                    swaps += 1
                #no perfect swap possible, find item that belongs here and swap this one away
                else:
                    j = index_dict[i+offset]
                    index_dict[arr[i]] = j
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
            except:
                pass
    return swaps
                
            
        
def proper_place(arr, i, min):
    return arr[i] - min == i



if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

# Jump Search
# Algorithm to search an element x in a sorted array arr
# Suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation from the index km to find the element x.

# Time Complexity = O(sqrt(n)) 

import math

def jump_search(arr, x, n):
    step = math.sqrt(n)
    prev = 0

    # check whether x is present in any interval of arr
    while arr[int(min(step, n)) - 1] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # if x is present in the range (prev, prev+step), we have to find its exact position
    for i in range(int(prev), int(prev+step)+1):
        if arr[i] == x:
            return i

    return -1



arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
index = jump_search(arr, x, len(arr))
print("Number" , x, "is at index" ,"%.0f"%index)

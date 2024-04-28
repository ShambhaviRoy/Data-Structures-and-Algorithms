# Magic Index: A magic index in an array A [1. .. n -1] is defined to be an index such that A[i] = i. 
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.
# FOLLOW UP
# What if the values are not distinct?


# Brute Force: Iterate over array and check for this condition
# Time complexity = O(n)
def magic_slow(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1



# Recursive: Linear
def magic_recursive(arr):
    return magic_recursive_help(arr, 0)

def magic_recursive_help(arr, i):
    if i == len(arr)-1:
        return -1
    if arr[i] == i:
        return i
    else:
        return magic_recursive_help(arr, i+1)



# Recursion with Binary search: If elements are distinct
def is_magic(arr):
    return is_magic_helper(arr, 0, len(arr)-1)

def is_magic_helper(arr, start, end):
    if end < start:
        return -1
    mid = (start + end)//2
    if(arr[mid] == mid):
        return mid
    elif arr[mid] > mid:
        # search left
        return is_magic_helper(arr, start, mid)
    else:
        # search right
        return is_magic_helper(arr, mid+1, end)
    

    

# Recursion with Binary search: If elements are not distinct
def is_magic2(arr):
    return magic2_helper(arr, 0, len(arr)-1)

def magic2_helper(arr, start, end):
    if(end < start):
        return -1
    mid_index = (start + end) // 2
    mid_value = arr[mid_index]
    if(mid_index == mid_value):
        return mid_value
    
    left_index = min(mid_index-1, mid_value)
    left = magic2_helper(arr, start, left_index)
    if(left >= 0):
        return left

    right_index = max(mid_index+ 1, mid_value)
    right = magic2_helper(arr, right_index, end)
    return right



arr = [-30, -10, 0, 3, 5, 16, 23]
print(magic_recursive(arr))
print(is_magic(arr))
print(is_magic2(arr))
# Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
# elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest
# such sequence).
# EXAMPLE
# Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
# Output: (3, 9)

# m < n
# m = 0, n = len(arr) - 1
# Advance m if prev no. < curr no.
# Advance n if prev no. < curr no. 

def find_unsorted_sequence(arr):
    end_left = find_end_of_left_subsequence(arr)
    if end_left >= len(arr) - 1:
        print('Already sorted')
        return
    start_right = find_start_of_right_subsequence(arr)

    # get min and max in the middle section
    max_index = end_left # max of left side
    min_index = start_right # min of right side
    for i in range(end_left + 1, start_right):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i

    left_index = shrink_left(arr, min_index, end_left) # elements in the left have to be smaller than middle and right parts
    right_index = shrink_right(arr, max_index, start_right)

    print(f'Answer = {left_index, right_index}')
    

def shrink_left(arr, min_index, end_left):
    comp = arr[min_index]
    for i in range(end_left - 1, -1, -1):
        if arr[i] >= comp:
            return i + 1
    return 0

def shrink_right(arr, max_index, start_right):
    comp = arr[max_index]
    for i in range(start_right, len(arr) -1):
        if arr[i] >= comp:
            return i - 1
    return len(arr) - 1


def find_end_of_left_subsequence(arr):
    # elements have to be increasing order starting from index 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return i - 1
    return len(arr) - 1


def find_start_of_right_subsequence(arr):
    # elements have to be in decreasing order starting from index len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            return i + 1
    return 0



arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
find_unsorted_sequence(arr)
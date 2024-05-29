# Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.


def matrix_search(matrix, x):
    m = len(matrix)
    n = len(matrix[0]) - 1
    row_num = 0
    while row_num >= 0 and row_num < m:
        row = matrix[row_num]
        if x < row[0]:
            row_num -= 1
        elif x > row[n]:
            row_num += 1
        else:
            return (row_num, binary_search(row, x))



def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            return mid


matrix = [[15, 20, 40, 85],
          [20, 35, 80, 95],
          [30, 55, 95, 105],
          [40, 80, 100, 120]]
x = 95
print(matrix_search(matrix, x))
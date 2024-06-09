# Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.


def matrix_search(matrix, x):
    row = 0
    col = len(matrix[0]) - 1
    while(row < len(matrix) and col  >= 0):
        if(matrix[row][col] == x):
            return (row, col)
        elif matrix[row][col] > x:
            col -= 1
        else:
            row += 1
    return (-1, -1)



matrix = [[15, 20, 40, 85],
          [20, 33, 80, 95],
          [30, 55, 95, 105],
          [40, 80, 100, 120]]
x = 33
print(matrix_search(matrix, x))
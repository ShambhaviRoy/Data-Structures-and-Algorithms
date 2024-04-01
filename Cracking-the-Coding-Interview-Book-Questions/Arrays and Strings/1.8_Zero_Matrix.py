# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

# Solution: We can reduce the space complexity to O(1) by using the first row as a replacement for the row array and the first column as a replacement for the column array.
# This works as follows:
# 1. Check if the first row and first column have any zeros, and set variables rowHasZero and columnHasZero. We'll nullify the first row and first column later, if necessary.
# 2. Iterate through the rest of the matrix, setting matrix[i][0] and matrix[0][j] to zero whenever there's a zero in matrix[i][j].
# 3. Iterate through rest of matrix, nullifying row i if there's a zero in matrix[i][0].
# 4. Nullify the first row and first column if necessary.


def setZero(matrix):
    rowHasZero = True if 0 in matrix[0][:] else False # Check if 1st row has zero
    colHasZero = True if 0 in matrix[:][0] else False # Check if 1st column has zero

    # Traverse through matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify rows based on value in first column
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            matrix = nullifyRow(matrix, i)

    # # Nullify colums based on value in first row
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            matrix = nullifyColumn(matrix, j)
    
    # Nullify first row and column if necessary (if a 0 has come in the first row/column in the previous steps)
    if rowHasZero:
        matrix = nullifyRow(matrix, 0)

    if colHasZero:
        matrix = nullifyColumn(matrix, 0)

    return matrix


def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
    return matrix

def nullifyColumn(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
    return matrix


matrix = [[1, 2, 3, 4],
            [5, 0, 7, 8],
            [9, 10, 11, 12]]
print("Original Matrix:")
print(matrix)
print("Zero Matrix:")
print(setZero(matrix))
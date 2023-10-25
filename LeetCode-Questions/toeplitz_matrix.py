# Check whether the given matrix is a Toeplitz matrix.
# A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are same.


def is_toeplitz(matrix):
    M = len(matrix) #no. of rows in matrix
    N = len(matrix[0]) #no. of columns in matrix

    i = 0
    d = 0

    while d < N:
        diag = matrix[0][i]
        j = i + 1
        while j < M:
            if matrix[i+1][j] != diag:
                return False
            j += 1
            i += 1
            print('----')
        d += 1
        N -= 1
    return True




matrix = [[1, 2, 3, 4], 
          [5, 1, 2, 3], 
          [6, 5, 1, 2], 
          [7, 6, 5, 1]]

print(is_toeplitz(matrix))
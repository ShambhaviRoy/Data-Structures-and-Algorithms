# Check whether the given matrix is a Toeplitz matrix.
# A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are same.

# Approach 1: Traverse each diagonal and compare with first value on the diagonal
# Time Complexity = O(m * n)
# Space Complexity = O(1)
def is_toeplitz(matrix):
    m = len(matrix)
    n = len(matrix[0])

    d = 0
    for d in range(m):
        diag = matrix[d][0]
        print(f'({d}, 0), diag = {diag}')
        i = 0
        while i+d < m and i < n:
            if diag != matrix[i+d][i]:
                return False
            else:
                i += 1

    d = 1
    for d in range(1, n):
        diag = matrix[0][d]
        print(f'(0, {d}), diag = {diag}')
        j = 0
        while j < m and j+d < n:
            if diag != matrix[j][j+d]:
                return False
            else:
                j += 1

    return True



# Approach 2: Grouping diagonals by value
# A diagonal is (0, 0), (1, 1), (2, 2), and so on.. so the difference (row - col) remains constant along the diagonal
# Time Complexity = O(m * n)
# Space Complexity = O(m + n)
def is_toeplitz2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    diagonals = {}

    for r in range(m):
        for c in range(n):
            if r - c not in diagonals:
                diagonals[r - c] = matrix[r][c]
            elif diagonals[r - c] != matrix[r][c]:
                return False
    return True


# Approach 3: Check with top-left value
# For each diagonal a1, a2, .. , an --> check whether a1 == a2, a2 == a3 and so on..
# Time Complexity = O(m * n)
# Space Complexity = O(1)
def is_toeplitz3(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for r in range(m):
        for c in range(n):
            if not (r == 0 or c == 0 or matrix[r - 1][c - 1] == matrix[r][c]):
                return False
    return True



matrix = [[1, 2, 3, 4], 
          [5, 1, 2, 3], 
          [6, 5, 1, 2], 
          [7, 6, 5, 1]]

print(is_toeplitz(matrix))
print(is_toeplitz2(matrix))
print(is_toeplitz3(matrix))
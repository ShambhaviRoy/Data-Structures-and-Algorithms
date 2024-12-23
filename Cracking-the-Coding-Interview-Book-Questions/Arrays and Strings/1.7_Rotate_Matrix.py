#Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


# Time Complexity = O(N^2), Space Complexity = O(N^2)
def rotate_matrix(matrix):
    if (len(matrix) == 0) or (len(matrix) != len(matrix[0])):
        return False
    
    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n -1-layer
        for i in range(first, last):
            offset = i- first
            top = matrix[first][i]

            #left -> top
            matrix[first][i] = matrix[last-offset][first]

            #bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            #right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            #top -> right
            matrix[i][last] = top
    return matrix

matrix = [[1, 2, 3, 4], 
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
print("Original Matrix:")
print(matrix)
print("Rotated Matrix:")
print(rotate_matrix(matrix))
# Given a matrix of integers, we'd like to consider the sum of the elements within the area of a 45° rotated rectangle. More formally, the area is bounded by two diagonals parallel to the main diagonal and two diagonals parallel to the secondary diagonal. The dimensions of the rotated rectangle are defined by the number of elements along the borders of the rectangle.

# Given integers a and b representing the dimensions of the rotated rectangle, and matrix (a matrix of integers), your task is to find the greatest sum of integers contained within an a x b rotated rectangle.

# Note: The order of the dimensions is not important - consider all a x b and b x a rectangles.

# For
# matrix = [[1, 2, 3, 4, 0],
#           [5, 6, 7, 8, 1],
#           [3, 2, 4, 1, 4],
#           [4, 3, 5, 1, 6]]
# a = 2, and b = 3, the output should be solution(matrix, a, b) = 36.
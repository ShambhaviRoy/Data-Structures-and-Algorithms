# https://www.facebook.com/careers/life/sample_interview_questions

# Question 1: 2D Spiral Array

def is_invalid(n, matrix, x, y):
    return x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] != -1

def spiral(n):
    if n <= 0:
        print('Invalid n')

    matrix = [[-1 for _ in range(n)] for _ in range(n)]
    value = 1
    r, c = 0, 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dir = 0

    while value <= (n*n):
        matrix[r][c] = value
        value += 1
        r += dr[dir]
        c += dc[dir]
        
        if is_invalid(n, matrix, r, c):
            r -= dr[dir]
            c -= dc[dir]
            dir = (dir+1)%4
            r += dr[dir]
            c += dc[dir]
    
    return matrix


print(spiral(3))
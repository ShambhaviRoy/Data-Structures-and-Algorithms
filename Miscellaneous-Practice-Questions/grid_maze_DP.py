def grid_maze_problem(grid, maxTime):
    answer = 'No'

    rows = len(grid)
    columns = len(grid[0])

    # create grid matrix
    grid_matrix = []

    for row in range(rows):
        grid_row = []
        for col in range(columns):
            grid_row.append(1e6)
        grid_matrix.append(grid_row)

    # print(grid_matrix)

    grid_matrix[0][0] = 0


    for i in range(1, rows):
        if grid[0][i] == '$':
            break
        grid_matrix[0][i] = grid_matrix[0][i-1] + 1


    for j in range(1, columns):
        if grid[j][0] == '$':
            break
        grid_matrix[j][0] = grid_matrix[j-1][0] + 1

    for i in range(1, rows):
        for j in range(1, columns):
            if grid[i][j] == '.':
                grid_matrix[i][j] = min(grid_matrix[i-1][j], grid_matrix[i][j-1]) + 1

    print(grid_matrix)

    if grid_matrix[rows-1][columns-1] <= maxTime:
        answer = 'Yes'

    return answer



if __name__ == '__main__':
    grid  = ['..$$', '$.$$', '$...']
    maxTime = 6
    print(grid_maze_problem(grid, maxTime))






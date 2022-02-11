# DFS on a 2D Matrix, can traverse in all 8 directions (top, down, left, right and diagonals)

visited = [[False for i in range(5)] for j in range(5)] # all coords unvisited
adj_x = 0
adj_y = 0

dRow = [0, 1, 1, 1, 0, -1, -1, -1]
dCol = [-1, -1, 0, 1, 1, 1, 0, -1]

def check_valid_coords(x, y):
    global visited

    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False

    if visited[x][y]:
        return False

    return True


def DFS(cell_x, cell_y, grid):

    global dRow
    global dCol
    global visited

    S = []
    S.append([cell_x, cell_y])

    while len(S) > 0:
       cell_x, cell_y = S[-1]
       S.pop()
       
       if check_valid_coords(cell_x, cell_y) == False:
            continue
       
       visited[cell_x][cell_y] = True

       print(grid[cell_x][cell_y])
        
       for i in range(8):
           adj_x = cell_x + dRow[i]
           adj_y = cell_y + dCol[i]
           S.append([adj_x, adj_y])


grid = [['R', 'A', 'E', 'L'], ['M', 'O', 'F', 'S'], ['T', 'E', 'O', 'K'], ['N', 'A', 'T', 'I']]

DFS(0, 0, grid)
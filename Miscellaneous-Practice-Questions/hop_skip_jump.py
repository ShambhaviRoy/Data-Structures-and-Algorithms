# Lucy loves to play the Hop. Skip and Jump game. Given an N∗M matrix and starting from cell (1,1), her challenge is to hop in an anti-clockwise direction and skip alternate cells. The goal is to find out the last cell she would hop onto. Write an algorithm to find the last cell Lucy would hop onto after moving anti-clockwise and skipping alternate cells.
# Input The first line of input consists of two integers: matrix_row and matrix col, representing the number of rows (N) and the number of columns (M) in the matrix, respectively. The next M lines consist of N space-separated integers representing the elements in each cell of the matrix. 
# Output Print an integer representing the last cell Lucy would hop onto after following the given instructions. 
# Example Input: 3 3 29 8 37 15 41 3 1 10 14 Output: 41 Explanation: Lucy starts with 29, skips 15, hops onto 1, skip 10, hops onto 14, skips 3, hops onto 37 , skips 8 and finally hops onto 41. So, the output is 41 .


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid_coordinate(x, y, grid, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited


def hop_skip_jump(grid):
    N = len(grid)
    M = len(grid[0])

    x, y = 0, 0
    curr_dir = 0

    visited = set()
    visited.add((0, 0))

    steps = 0
    hops = []
    last_hop = grid[x][y]

    fail_attempts = 0
    while True:
        dx, dy = directions[curr_dir]
        new_x, new_y = x + 2*dx, y + 2*dy

        if is_valid_coordinate(new_x, new_y, grid, visited):
            x, y = new_x, new_y
            hops.append((x, y))
            visited.add((x, y))
            steps += 1
            fail_attempts = 0
        else:
            curr_dir = (curr_dir + 1) % 4
            if fail_attempts > 4:
                break
            fail_attempts += 1

    print(hops)
    return grid[hops[-1][0]][hops[-1][1]]



grid = [[29, 8, 37], [15, 41, 3], [1, 10, 14]]
print(hop_skip_jump(grid))
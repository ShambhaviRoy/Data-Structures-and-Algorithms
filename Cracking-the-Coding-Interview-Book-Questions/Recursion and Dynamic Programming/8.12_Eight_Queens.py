# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.

GRID_SIZE = 8

def place_queens(row, columns, results):
    if row == GRID_SIZE:
        results.append(row)
    else:
        for col in range(GRID_SIZE):
            if(check_valid(columns, row, col)):
                columns[row] = col
                place_queens(row+1, columns, results)


def check_valid(columns, row1, col1):
    for row2 in range(row1):
        col2 = columns[row2]
        # check same column
        if col2 == col1:
            return False
        
        # check diagonal
        col_dist = abs(col1 - col2)
        row_dist = row1 - row2
        if row_dist == col_dist:
            return False
    return True

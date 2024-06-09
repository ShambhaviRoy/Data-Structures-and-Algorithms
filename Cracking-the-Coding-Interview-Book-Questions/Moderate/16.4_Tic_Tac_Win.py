# Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.

from enum import Enum

class Piece(Enum):
    EMPTY = 0
    RED = 1
    BLUE = 2


def winner(board, row, column):
    # (row, column) are co-ordinates of last move
    # edge case
    if(len(board) != len(board[0])):
        return Piece.EMPTY
    
    piece = board[row][column]
    if(piece == Piece.EMPTY):
        return Piece.EMPTY
    
    print(has_won_column(board, column))
    
    if(has_won_row(board, row) or has_won_column(board, column)):
        return piece
    
    if((row == column) and has_won_diagonal(board, 1)):
        return piece
    
    if((row == len(board) - column - 1) and has_won_diagonal(board, -1)):
        return piece

    return Piece.EMPTY

def has_won_row(board, row):
    for c in range(len(board)):
        if board[row][0] != board[row][c]:
            return False
    return True

def has_won_column(board, column):
    for r in range(len(board)):
        if board[0][column] != board[r][column]:
            return False
    return False

def has_won_diagonal(board, direction):
    row = 0
    if direction == 1:
        col = 0
    else:
        col = len(board) - 1
    first = board[row][col]
    for i in range(len(board)):
        if board[i][col] != first:
            return False
        row += 1
        col += direction
    return True


board = [[Piece.EMPTY, Piece.RED, Piece.BLUE],
         [Piece.BLUE, Piece.RED, Piece.EMPTY],
         [Piece.EMPTY, Piece.RED, Piece.BLUE]]

print(winner(board, 2, 1))
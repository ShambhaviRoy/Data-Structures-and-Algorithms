# Knight's tour
# https://nados.io/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/9c432afc-f3ff-4c3c-95a5-f2aca5ecfc1a/question/723c19f6-1ab7-4a87-badf-1c36d5ab5831

# 1. You are given a number n, the size of a chess board.
# 2. You are given a row and a column, as a starting point for a knight piece.
# 3. You are required to generate the all moves of a knight starting in (row, col) such that knight visits 
#      all cells of the board exactly once.
# 4. Complete the body of printKnightsTour function - without changing signature - to calculate and 
#      print all configurations of the chess board representing the route
#      of knight through the chess board.


def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], "", end='')  
        print()
    print()
    
    
def printKnightsTour(chess,n,r,c,upcomingMove):
    # invalid combinations
    if r<0 or r>=n or c<0 or c>=n or chess[r][c] > 0:
        return

    if upcomingMove == (n*n):
        chess[r][c] = upcomingMove
        displayBoard(chess)
        chess[r][c] = 0
        return
    

    chess[r][c] = upcomingMove

    printKnightsTour(chess, n, r-2, c+1, upcomingMove+1)   #1
    printKnightsTour(chess, n, r-1, c+2, upcomingMove+1)   #2
    printKnightsTour(chess, n, r+1, c+2, upcomingMove+1)   #3
    printKnightsTour(chess, n, r+2, c+1, upcomingMove+1)   #4
    printKnightsTour(chess, n, r+2, c-1, upcomingMove+1)   #5
    printKnightsTour(chess, n, r+1, c-2, upcomingMove+1)   #6
    printKnightsTour(chess, n, r-1, c-2, upcomingMove+1)   #7
    printKnightsTour(chess, n, r-2, c-1, upcomingMove+1)   #8

    chess[r][c] = 0

    

if __name__ == '__main__':
    n=int(input())  
    chess=[]  
    for i in range(n):
        a=[]  
        for j in range(n):
            a.append(0)  
        chess.append(a)  
    row=int(input())      
    col=int(input())   
    printKnightsTour(chess,n,row,col,1)  

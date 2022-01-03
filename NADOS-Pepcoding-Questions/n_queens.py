# N Queens
# https://nados.io/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/9c432afc-f3ff-4c3c-95a5-f2aca5ecfc1a/question/726d3e2f-21fc-4b68-a2eb-45d67cfadd0d

# 1. You are given a number n, the size of a chess board.
# 2. You are required to place n number of queens in the n * n cells of board such that no queen can kill another.
# Note - Queens kill at distance in all 8 directions
# 3. Complete the body of printNQueens function - without changing signature - to calculate and print all safe configurations of n-queens. 

# Constraints: 1 <= n <= 10

def printNQueens(chess,qsf,row):
    #base case
    if row == len(chess):
        print(qsf+'.')
        return


    for col in range(len(chess)):
        if isQueenSafe(chess, row, col) == True: 
            # place queen
            chess[row][col] = 1

            # recursive call to explore
            printNQueens(chess, qsf+str(row)+'-'+str(col)+', ', row+1)

            # unplace
            chess[row][col] = 0 



def isQueenSafe(chess, row, col):
    # to check if it is safe to place queen in chess[row][col]
    # top
    r = row
    c = col
    while r>=0:
        if chess[r][c] == 1:
            return False
        r -= 1

    # top left
    r = row
    c = col
    while r>=0 and c>=0:
        if chess[r][c] == 1:
            return False
        r-=1
        c-=1

    # top right
    r = row
    c = col
    while r>=0 and c <len(chess):
        if chess[r][c] == 1:
            return False
        r-=1
        c+=1

    return True



if __name__ == '__main__':
    chess=[] 
    n = int(input()) 
    for i in range(n):          
        a =[]
        for j in range(n): 
            a.append(0) 
        chess.append(a)
    printNQueens(chess,"",0) 

    

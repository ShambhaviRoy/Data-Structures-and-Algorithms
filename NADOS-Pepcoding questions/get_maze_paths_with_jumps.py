# Get Maze Paths with Jumps
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/b0de95ee-d178-450a-b3a0-325eeaccfa58/question/a6a44362-0973-4003-a556-b1225e979e75

# 1. You are given a number n and a number m representing number of rows and columns in a maze.
# 2. You are standing in the top-left corner and have to reach the bottom-right corner. 
# 3. In a single move you are allowed to jump 1 or more steps horizontally (as h1, h2, .. ), or 1 or more steps vertically (as v1, v2, ..) or 1 or more steps diagonally (as d1, d2, ..). 
# 4. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.

# Constraints
# 0 <= n <= 10
# 0 <= m <= 10


def get_maze_paths(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        return ['']

    answer = []

    # horizontal move
    for k in range(1, dc+1):
        if sc+k <= dc:
            horizontal_paths = get_maze_paths(sr, sc+k, dr, dc)
            for hp in horizontal_paths:
                new_path = 'h' + str(k) + hp
                answer.append(new_path)


    # vertical move
    for k in range(1, dr+1):
        if sr+k <= dr:
            vertical_paths = get_maze_paths(sr+k, sc, dr, dc)
            for vp in vertical_paths:
                new_path = 'v' + str(k) + vp
                answer.append(new_path)   

        
    # diagonal move
    for k in range(1, max(dr, dc) + 1):
        if sr+k <= dr and sc+k <= dc:
            diagonal_paths = get_maze_paths(sr+k, sc+k, dr, dc)
            for dp in diagonal_paths:
                new_path = 'd' + str(k) + dp
                answer.append(new_path)

        
    return answer



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    ans = get_maze_paths(0,0,n-1,m-1)
    print("["+', '.join(ans) + "]")

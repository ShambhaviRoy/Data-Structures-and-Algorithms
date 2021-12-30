# Get Maze Paths
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/b0de95ee-d178-450a-b3a0-325eeaccfa58/question/55bb58e5-927d-4210-b1eb-ce74735d1364

# 1. You are given a number n and a number m representing number of rows and columns in a maze.
# 2. You are standing in the top-left corner and have to reach the bottom-right corner. Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
# 3. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.

# Constraints
# 0 <= n <= 10
# 0 <= m <= 10



def get_maze_path(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        return ['']

    answer = []

    if dc >= 1 + sc:
        # horizontal move
        horizontal_ans = get_maze_path(sr, sc+1, dr, dc)
        for element in horizontal_ans:
            answer.append('h' + element)        

    if dr >= 1 + sr:
        # vertical move
        vertical_ans = get_maze_path(sr+1, sc, dr, dc)
        for element in vertical_ans:
            answer.append('v' + element)
    
    # print(answer)

    return answer



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    ans = get_maze_path(0,0,n-1,m-1)
    print("["+', '.join(ans) + "]")

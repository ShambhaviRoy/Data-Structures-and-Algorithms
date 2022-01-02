# Flood Fill
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/9c432afc-f3ff-4c3c-95a5-f2aca5ecfc1a/question/eac2a729-6416-4858-93a7-244c0cd57302

# 1. You are given a number n, representing the number of rows.
# 2. You are given a number m, representing the number of columns.
# 3. You are given n*m numbers, representing elements of 2d array maze. The numbers can be 1 or 0 only.
# 4. You are standing in the top-left corner and have to reach the bottom-right corner. 
# Only four moves are allowed 't' (1-step up), 'l' (1-step left), 'd' (1-step down) 'r' (1-step right). You can only move to cells which have 0 value in them. You can't move out of the boundaries or in the cells which have value 1 in them (1 means obstacle)
# 5. Complete the body of floodfill function - without changing signature - to print all paths that can be used to move from top-left to bottom-right.

# If all four moves are available make moves in the order 't', 'l', 'd' and 'r'        

# Constraints
# 1 <= n <= 10
# 1 <= m <= 10
# e1, e2, .. n * m elements belongs to set (0, 1)


# asf -> answer so far
def floodfill(maze, sr, sc, asf, visited, n, m):
  if (sr<0 or sc<0 or sr>=n or sc>=m or maze[sr][sc]==1 or visited[sr][sc]==True):
    return
  
  if sr == n-1 and sc == m-1:
    print(asf)
    return 

  visited[sr][sc] = True

  floodfill(maze, sr-1, sc, asf+'t', visited, n, m)
  floodfill(maze, sr, sc-1, asf+'l', visited, n, m)
  floodfill(maze, sr+1, sc, asf+'d', visited, n, m)
  floodfill(maze, sr, sc+1, asf+'r', visited, n, m)

  visited[sr][sc] = False


if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = []
    for i in range(n):          
        row = list(map(int, input().split()))
        arr.append(row)

    visited = []
    for i in range(n):          
        a =[]
        for j in range(m): 
            a.append(False)
        visited.append(a)

    floodfill(arr, 0, 0, "", visited, n, m)
 
# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.


def get_path(maze):
    # base case
    if(not maze or len(maze) == 0):
        return None

    path = []
    visited_points = []
    if(get_path_helper(maze, len(maze)-1, len(maze[0])-1, path, visited_points)):
        return path
    return None


def get_path_helper(maze, r_start, c_start, path, visited_points):
    # base case
    if(r_start < 0 or c_start < 0 or not maze[r_start][c_start]):
        return False
    
    p = (r_start, c_start)
    if(p in visited_points):
        return False
    
    if r_start == 0 and c_start == 0:
        is_at_origin = True
    else:
        is_at_origin = False

    # if there is a path from start to current location, add current location to path
    if(is_at_origin or get_path_helper(maze, r_start, c_start-1, path, visited_points) 
       or get_path_helper(maze, r_start-1, c_start, path, visited_points)):
        path.append(p)
        return True
    
    visited_points.append(p)
    return False


maze = [[True, True, False, False, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True]]

print(get_path(maze))
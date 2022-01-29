# Given start coordinates = (a, b) and end coordinates = (c, d), and allowed moves are:
# (a, b) --> (a+b, b) and (a, b) --> (a, a+b) 
# Then find whether it's possible to go from (a, b) to (c, d). Return True/False.

# Idea:
# We trace a path from end point to start point so we can find only 1 way to go back
# This problem can be visualized as a tree problem: 
# If start = (3, 7) and end = (64, 27), the path is: (64, 27) -> (10, 27) -> (10, 7) -> (3, 7)
# that is (64, 27) -> (64%27, 27) -> (10, 27%10) -> (10%7, 7)
# Conditions: 
#   If target x (c) > target y (d), we go back to (c%d, d) else we go back to (c, d%c)
#   If start x (a) == target x (c), we can traverse only along y-axis by (d-b) steps and checking if that (d-b)%a==0 (reaching starting point)
#   If start y (b) == target y (d), we can traverse only along x-axis by (c-a) steps and checking if that (c-a)%b==0 (reaching starting point) 
# Base case: If end point coordinates are lesser than start point coordinates, can't go back


def can_go(a, b, c, d):

    if c < a or d < b:
        return False
        
    if a == c:
        return ((d - b) % a) == 0
    elif b == d:
        return ((c - a) % b) == 0
    
    if c > d:
        return can_go(a, b, c%d, d)
    else:
        return can_go(a, b, c, d%c)



if __name__ == '__main__':
    print('Enter start coordinates:')
    a = int(input())
    b = int(input())

    print('Enter end coordinates:')
    c = int(input())
    d = int(input())

    result = can_go(a, b, c, d)
    print(result)


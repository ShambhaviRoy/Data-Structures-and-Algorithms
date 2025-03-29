# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

# https://leetcode.com/problems/detect-squares/description/

# Time Complexity of add = O(1)
# Time Complexity of count = O(n) (much lesser in practice)
# Space Complexity = O(n)

from collections import Counter, defaultdict

class DetectSquares:
    
    def __init__(self):
        self.points_map = Counter()
        self.x_coord = defaultdict(set)
        

    def add(self, point) -> None:
        x, y = point
        self.points_map[(x, y)] += 1
        self.x_coord[x].add(y)

        
        
    def count(self, point) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.x_coord[x1]:
            if y1 == y2:
                continue
            side_length = abs(y2 - y1)
            # 2 options for x2 (above and below x1)
            x2a = x1 + side_length
            x2b = x1 - side_length
            ans += self.points_map[(x1, y2)] * self.points_map[(x2a, y2)] * self.points_map[(x2a, y1)]
            ans += self.points_map[(x1, y2)] * self.points_map[(x2b, y2)] * self.points_map[(x2b, y1)]

        return ans

        
        


obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
obj.add([11,10])
count1 = obj.count([14,8])
print(count1)
obj.add([11,2])
count2 = obj.count([11,10])
print(count2)

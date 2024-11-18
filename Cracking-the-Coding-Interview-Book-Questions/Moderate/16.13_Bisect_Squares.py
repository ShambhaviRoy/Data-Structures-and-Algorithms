# Bisect Squares: Given two squares on a two-dimensional plane, find a line that would cut these two
# squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def extend_line(self, other, size):
        # extend a line from one point to another
        xdir = -1 if self.x < other.x else 1
        ydir = -1 if self.y < other.y else 1
        if self.x == other.x:
            return Point(self.x, other.y + ydir * size / 2)
        slope = (other.y - self.y)/(other.x - self.x)
        x1 = 0
        y1 = 0
        if(abs(slope) == 1):
            x1 = self.x + xdir * size / 2
            y1 = self.y + ydir * size / 2
        elif abs(slope) < 1:
            x1 = self.x + xdir * size / 2
            y1 = slope * (x1 - self.x) + self.y
        else:
            y1 = self.y + ydir * size / 2
            x1 = (y1 - self.y) / slope * self.x
        return Point(x1, y1) 

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_ends(self):
        print(f'Start = {self.start}, End = {self.end}')

class Square:
    def __init__(self, top_left, top_right, bottom_left, bottom_right, size):
        # extremities
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.size = size

    def middle(self):
        x = (self.top_left.x + self.bottom_right.x)/2
        y = (self.top_right.y + self.bottom_right.y)/2
        return Point(x, y)

    def cut(self, other):
        # to find line bisecting self and other (Squares)
        mid1 = self.middle
        mid2 = other.middle
        p1 = mid1.extend_line(mid2, self.size)
        p2 = mid1.extend_line(mid2, -1 * self.size)
        p3 = mid2.extend_line(mid1, self.size)
        p4 = mid2.extend_line(mid1, -1 * self.size) 
        start = p1
        end = p1
        # start is farthest left and end is farthest right (of p1, .., p4)
        for point in [p2, p3, p4]:
            if start.x > point.x:
                start = point
            if end.x < point.x:
                end = point

        return Line(start, end)
    


s1 = Square(Point(1, 2), Point(2, 2), Point(1, 1), Point(2, 1), 1)
s2 = Square(Point(4, 4), Point(8, 4), Point(4, 0), Point(8, 0), 4)
line = s1.cut(s2)
line.print_ends()
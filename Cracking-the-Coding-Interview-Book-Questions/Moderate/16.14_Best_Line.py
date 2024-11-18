# Best Line: Given a two-dimensional graph with points on it, find a line which passes the most
# number of points.

from collections import defaultdict

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f'x = {self.x}, y = {self.y}')


class Line:
    def __init__(self, point1, point2):
        self.slope = 0
        self.intercept = 0
        self.epsilon = 0.001
        self.infinite_slope = False

        if(abs(point1.x - point2.x) > self.epsilon):
            self.slope = (point2.y - point1.y) / (point2.x - point1.x)
            self.intercept = point1.y - self.slope * point1.x
        else:
            self.infinite_slope = True
            self.intercept = 0

    def print_line(self):
        print(f'Slope = {self.slope}, intercept = {self.intercept}, Infinite slope = {self.infinite_slope}')    

    def floor_to_nearest_epsilon(self):
        r = int(self.slope / self.epsilon)
        return r * self.epsilon 
    
    def is_equivalent_slope(self, other):
        return abs(self.slope - other.slope) < self.epsilon
    
    def is_equivalent(self, other):
        return self.is_equivalent_slope(other) and (self.intercept == other.intercept) and (self.infinite_slope == other.infinite_slope)
        


# find the lines between all points, the line passing through most points (count) is the answer
def find_best_line(points):
    lines_by_slope = get_lines_by_slope(points)
    for s in lines_by_slope.keys():
        llist = lines_by_slope[s]
    return get_best_line(lines_by_slope)

# use each pair of points and form a line
def get_lines_by_slope(points):
    lines_by_slope = defaultdict(list)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            line = Line(points[i], points[j])
            key = line.floor_to_nearest_epsilon()
            lines_by_slope[key].append(line)
    return lines_by_slope


# find the line with most equivalent other lines
def get_best_line(lines_by_slope):
    best_line = None
    best_count = 0
    slopes = list(lines_by_slope.keys())
    for slope in slopes:
        lines = lines_by_slope[slope]
        for line in lines:
            count = get_equivalent_lines(lines_by_slope, line)
            if count > best_count:
                best_count = count
                best_line = line
    return best_line


# check map for equivalent lines, i.e. lines with slopes within 1 epsilon of each other
def get_equivalent_lines(lines_by_slope, line : Line):
    key = line.floor_to_nearest_epsilon()
    count = len(lines_by_slope[key])
    count += count_equivalent_lines(lines_by_slope[key + line.epsilon], line)
    count += count_equivalent_lines(lines_by_slope[key - line.epsilon], line)
    return count

        
# check list for equivalent lines, i.e. lines with slopes within 1 epsilon of each other
def count_equivalent_lines(lines : list[Line], line : Line):
    if len(lines) == 0:
        return 0
    count = 0
    for parallel_line in lines:
        if line.is_equivalent(parallel_line):
            count += 1
    return count


point1 = Point(1, 1)
point2 = Point(2, 2)
point3 = Point(-1, 3)
point4 = Point(4, 10)

points = [point1, point2, point3, point4]
line = find_best_line(points)
line.print_line()

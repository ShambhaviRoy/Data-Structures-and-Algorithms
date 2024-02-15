# Intersection: Given two straight line segments (represented as a start point and an end point),
# compute the point of intersection, if any.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("x = ", self.x, ", y = ", self.y)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        if(self.start.x == self.end.x):
            self.slope = float('inf')
            self.y_intercept = float('inf')
        else:
            self.slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
            self.y_intercept = self.end.y - (self.slope * self.end.x)

    def is_vertical(self):
        if(self.slope == float('inf')):
            return True
        return False
    
    def get_y_from_x(self, x):
        if(self.slope == float('inf')):
            return float('inf')
        else:
            return self.y_intercept + self.slope * x


class Question:
    def check_in_between(self, start, middle, end):
        if(start < end):
            return start <= middle and middle <= end
        else:
            return end <= middle and middle <= start
        

    def point_in_between(self, start, middle, end):
        return self.check_in_between(start.x, middle.x, end.x) and self.check_in_between(start.y, middle.y, end.y)
    

    def find_intersection(self, start1, end1, start2, end2):
        line1 = Line(start1, end1)
        line2 = Line(start2, end2)

        if(line1.slope == line2.slope):
            return 0
        
        if(self.point_in_between(start1, start2, end1)):
            return start2
        if(self.point_in_between(start2, start1, end2)):
            return start1
        if(self.point_in_between(start1, end2, end1)):
            return end2
        if(self.point_in_between(start2, end1, start2)):
            return end1
        
        if(line1.is_vertical):
            x = line1.slope
        elif(line2.is_vertical):
            x = line2.slope
        else:
            x = (line2.y_intercept - line1.y_intercept)/(line1.slope - line2.slope)

        if(line1.is_vertical):
            y = line2.get_y_from_x(x)
        else:
            y = line1.get_y_from_x(x)
        
        intersection = Point(x, y)

        if(self.point_in_between(start1, intersection, end1) and self.point_in_between(start2, intersection, end2)):
            return intersection

        return None

        
    

if __name__ == "__main__":
    start1 = Point(1, 2)
    end1 = Point(5, 6)
    start2 = Point(-3, 4)
    end2 = Point(10, 3)

    q = Question()

    Point.print_point(q.find_intersection(start1, end1, start2, end2))
    
    
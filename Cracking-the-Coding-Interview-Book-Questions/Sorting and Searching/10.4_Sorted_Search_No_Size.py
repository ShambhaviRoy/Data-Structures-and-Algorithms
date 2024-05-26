# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method. It does, however, have an elementAt (i) method that returns the element at index i in
# O(1) time. If i is beyond the bounds of the data structure, it returns - 1. (For this reason, the data
# structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.


class Listy:
    def __init__(self):
        self.listy = []

    def add(self, x):
        try:
            if x > 0:
                self.listy.append(x)
        except:
            pass
        
    def elementAt(self, i):
        try:
            return self.listy[i]
        except:
            return -1
        
    def find_last_index(self, max_size):
        low = 0
        high = max_size
        while low <= high:
            mid = (low + high)//2
            if self.elementAt(mid) != -1 and self.elementAt(high) == -1:
                low = mid + 1
            elif self.elementAt(low) != -1 and self.elementAt(mid) == -1:
                high = mid
            else:
                return mid

    
    def sorted_search(self, x, max_size):
        low = 0
        high = self.find_last_index(max_size)
        while low <= high:
            mid = (low + high)//2
            if self.listy[mid] < x:
                low = mid + 1
            elif self.listy[mid] > x or self.listy[mid] == -1:
                high = mid
            else:
                return mid
        return -1




listy = Listy()
listy.add(1)
listy.add(3)
listy.add(6)
listy.add(8)
listy.add(10)
listy.add(15)
print(listy.find_last_index(100))
print(listy.sorted_search(8, 100))
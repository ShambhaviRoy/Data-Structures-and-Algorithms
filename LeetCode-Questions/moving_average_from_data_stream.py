# 346. Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# https://leetcode.com/problems/moving-average-from-data-stream/description/

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5], [2]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0, 3.3333]

# [] -> (Moving average = None)
# [1] -> (Moving average = 1.0)
# [1, 10] -> (Moving average = 5.5)
# [1, 10, 3] -> (Moving average = 4.66667)
# [1, 10, 3, 5]  -> [10, 3, 5] -> (Moving average = 6.0)
# [10, 3, 5, 2]  -> [3, 5, 2] -> (Moving average = 3.3333)


from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.capacity = size
        self.stream = deque()
        self.window_size = 0
        self.window_sum = 0 # to store the sum of elements in window at any time


    def next(self, val: int):
        # add incoming val to stream
        self.stream.append(val)
        self.window_size += 1
        # calculate average of last capacity items of window
        if self.capacity >= self.window_size:
            tail = 0
        else:
            # pop out the oldest item from window and calculate average of the last capacity items
            tail = self.stream.popleft()
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.capacity, self.window_size)


mv = MovingAverage(3)
print(mv.next(1))
print(mv.next(10))
print(mv.next(3))
print(mv.next(5))
print(mv.next(2))
# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

# Approach:
# A min-heap to store upper half elements --> so the heap top is the minimum of the upper half of the elements
# And a max-heap to store lower half elements --> so the heap top is the maximum of the lower half of the elements
# So if both heaps are equal sized, the median is the heap top
# But if the heap sized are not equal, the median is the average of both heap tops

import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        max_of_lower_half = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_of_lower_half)
        if len(self.min_heap) > len(self.max_heap):
            min_of_upper_half = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_of_upper_half)


    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return self.min_heap[0]
        else:
            mid1 = self.min_heap[0]
            mid2 = -self.max_heap[0]
            return (mid1 + mid2) / 2
        

commands = ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
median_finder = MedianFinder()
for command in commands[1:]:
    if command == "addNum":
        num = int(input("Enter number:"))
        median_finder.add_num(num)
    if command == "findMedian":
        print(median_finder.find_median())



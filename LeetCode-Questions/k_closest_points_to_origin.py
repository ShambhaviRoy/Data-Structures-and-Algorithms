# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# https://leetcode.com/problems/k-closest-points-to-origin/description/

# Approach: We need the k closest points and don't need further points --> max heap, iterate and push/pop on heap as per distance values
# Time complexity = O(n log k)
# Space complexity = O(k)

import heapq

class HeapElement:
    def __init__(self, dist, x, y):
        self.dist = dist
        self.point = (x, y)

    def __lt__(self, other):
        return self.dist > other.dist


def distance(x, y):
    return x ** 2 + y ** 2


def k_closest(points, k):
    max_heap = []

    for i, point in enumerate(points):
        x, y = point
        dist = distance(x, y)
        if i < k:
            element = HeapElement(dist, x, y)
            heapq.heappush(max_heap, element)
        else:
            top = max_heap[0]
            if top.dist > dist:
                element = HeapElement(dist, x, y)
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, element)

    return [h.point for h in max_heap]



points = [[1,3],[-2,2]]
k = 1
print(k_closest(points, k))


points = [[3,3],[5,-1],[-2,4]]
k = 2
print(k_closest(points, k))

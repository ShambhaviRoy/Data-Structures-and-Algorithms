# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# https://leetcode.com/problems/merge-intervals/description/


# Time complexity = O(n)
# Space complexity = O(n)
def merge_intervals(intervals):
    merged = []

    intervals.sort(key = lambda x: x[0])

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            # if intervals are spaced out
            merged.append(interval)
        else:
            # overlap
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))
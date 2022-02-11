# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:   # no overlap
            merged.append(interval)
        else:   # overlap
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    print("Enter no. of intervals")
    i = int(input())
    print('Enter intervals')

    intervals = []
    for _ in range(i):
        intervals.append(input())

    print(merge(intervals))


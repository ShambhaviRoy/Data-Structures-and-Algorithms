# Activity selection
# Input is a collection of intervals having [start time, finish time]
# Output should be a list of intervals such that the finish time of an interval is less than the start time of the previous interval
# Have to return the maximum possible intervals

# Greedy algorithm
# Earliest start is not the best

# Time Complexity = O(n log n)

def activity_selection(arr):
    if len(arr) == 0:
        return []
    
    if len(arr) == 1:
        return arr[0]

    # Sorted activities as per their finish time
    arr.sort(key = lambda x : x[1])

    # find interval 'a' with the smallest finish time in arr
    a = arr[0]
    i = 0
    ans = []
    ans.append(a)

    # consider further activities
    # if the start time of the new activity is greater than finish time of the previous one, it is non-overlapping and added to ans
    for j in range(1, len(arr)):
        if arr[j][0] >= arr[i][1]:
            ans.append(arr[j])
            i = j   # so we consider activities after the current one

    return ans



arr = [[1, 6], [2, 5], [3, 7], [4, 8], [8, 10]]
print(activity_selection(arr))


# Find the minimum length unsorted subarray which makes the given array sorted

# find starting index 'start' (scan from left to right)
# find ending index 'end' (scan from right to left)


def find_subarray_length(arr):
    n = len(arr)
    # start and end are the start and end indices of a candidate subarray
    start, end = 0, n-1
    
    # find start
    for start in range(n-1):
        if arr[start+1] < arr[start]:
            break
    
    if start == n-1:
        return (n-1, n-1)

    # find end
    for end in range(n-1, 0, -1):
        if arr[end-1] > arr[end]:
            break

    # to check whether sorting the subarray arr[start:end] makes arr sorted
    # find max and min element in arr[start:end]
    maximum = max(arr[start : end+1])
    minimum = min(arr[start : end+1])

    # if there's an element greater than minimum in arr[0:start], change start to element index
    for i in range(start):
        if arr[i] > minimum:
            start = i
            break

    # if there's an element lesser than maximum in arr[end:n-1], change end to element index
    for i in range(n-1, 0, -1):
        if arr[i] < maximum:
            end = i
            break

    return (start, end)


arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(find_subarray_length(arr))
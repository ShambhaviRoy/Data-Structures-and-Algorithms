# For any given array, find a summary of ranges in it
# You are given a sorted unique integer array arr.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
# Example: arr = [0, 1, 2, 4, 5, 7]
# Output = ['0->2', '4->5', '7']


# Time Complexity = O(n)
# Space Complexity = O(n)

def find_ranges(arr):
    ans = []

    # start and end are pointers to the beginning and end of range
    # i is used to traverse arr

    start, end, i = 0, 0, 0
    n = len(arr)

    while i < n:
        start = end = i

        while end < n-1 and arr[end] + 1 == arr[end + 1]:
            end += 1
        
        ans.append((str(arr[start])) + ('->' + str(arr[end]))*(start != end))

        i = end + 1

    return ans


if __name__ == '__main__':
    print('Enter length of arr:')
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    print(find_ranges(arr))

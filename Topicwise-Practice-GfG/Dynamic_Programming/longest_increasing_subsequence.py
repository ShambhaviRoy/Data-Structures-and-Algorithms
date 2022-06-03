# Find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
# Example: Length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}. 


# Approach: Dynamic Programming
# The length of LIS till index i is stored as lookup[i]
# The maximum value in lookup is the length of LIS
# Time Complexity = O(n^2), Space Complexity = O(n)

def find_lis_length(arr):
    n = len(arr)
    lookup = [1]*n

    for i in range(n):
        for j in range(0, i):
            if arr[i] > arr[j] and lookup[i] < lookup[j] + 1:
                lookup[i] = lookup[j] + 1
    
    return max(lookup)


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", find_lis_length(arr))



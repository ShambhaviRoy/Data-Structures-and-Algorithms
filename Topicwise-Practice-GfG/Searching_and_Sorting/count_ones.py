# Count no. of ones in a sorted binary array (0s and 1s) in non-increasing order 

# Approach 1: Prefix Sum
# Maintain an array (prefix_arr) to save the no. of ones from start to that index
# No. of ones = prefix_arr[n-2]

# Time Complexity = O(n)

def find_ones_prefix_arr(arr):
    n = len(arr)
    prefix_arr = [0]*(n+1)
    prefix_arr[0] = arr[0]

    for i in range(1,n):
        prefix_arr[i] = prefix_arr[i-1] + arr[i]

    print(prefix_arr)
    return prefix_arr[-2]




# Approach 2: Use binary search
# Find the last occurrence of 1s

# Time Complexity = O(log n)

def binary_search(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == 1 and arr[mid+1] == 0:
            return mid+1

        if arr[mid] == 0:
            return binary_search(arr[0:mid+1])
        
        return binary_search(arr[mid+1, high])

    return 0


arr=[1, 1, 1, 1, 0, 0, 0]
print(find_ones_prefix_arr(arr))
print(binary_search(arr))     

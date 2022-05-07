# Ternary Search
# Like binary search but instead divides the array into 3 subparts

# Time Complexity = O(log3 n)

def ternary_search(arr, x, low, high):
    if low <= high:
        # mid1 and mid2 mark the 2 points which divide arr in 3 parts
        mid1 = low + (high-low)//3
        mid2 = mid1 + (high-low)//3

        if arr[mid1] == x:
            return mid1

        if arr[mid2] == x:
            return mid2

        if arr[mid1] > x:
            # x is present in the lowest one-third of arr
            return ternary_search(arr, x, 0, mid1)
        if arr[mid2] < x:
            # x is present in the highest one-third of arr
            return ternary_search(arr, x, mid2+1, high)
        else:
            # x is present between mid1 and mid2
            return ternary_search(arr, x, mid1+1, mid2-1)

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
index = ternary_search(arr, x, 0, len(arr))
print(index)
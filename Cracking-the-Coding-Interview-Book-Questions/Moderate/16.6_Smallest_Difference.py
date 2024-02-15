# Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.
# EXAMPLE
# Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# Output: 3. That is, the pair (11 , 8).


# Brute force 1: Iterate over arr1 and arr2 and find differences
# Time complexity = O(n^2), Space complexity = O(1)
def find_smallest_difference1(arr1, arr2):
    # base case
    if(len(arr1) == 0 or len(arr2) == 0):
        return -1

    ans = float('inf')

    for num1 in arr1:
        for num2 in arr2:
            diff = abs(num1 - num2)
            ans = min(diff, ans)

    return ans



# Brute force 2: Sort arr1 and arr2, and traverse both together, find differences, move indices
# Time complexity = O(n^2), Space complexity = O(1)
def find_smallest_difference2(arr1, arr2):
    # base case
    if(len(arr1) == 0 or len(arr2) == 0):
        return -1
    
    arr1.sort()
    arr2.sort()

    ans = float('inf')
    i = 0
    j = 0

    while(i < len(arr1) and j < len(arr2)):
        diff = abs(arr1[i] - arr2[j])
        ans = min(diff, ans)
        if(arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1

    return ans


# Binary Search: Sort arr1, Iterate over arr2 to find closest element in arr1 to current element of arr2, update difference
# Time complexity = O(n log n), Space complexity = O(1)
def find_closest(arr, target):
    low = 0
    high = len(arr)-1
    
    while(low <= high):
        mid = (low + high)//2
        if(target > arr[low] and target < arr[mid]):
            high = mid - 1
        elif(target > arr[mid]):
            low = mid+1
        else:
            return arr[mid]
        
    if(low <= 0 or low >= len(arr)):
        value1 = float('inf')
    else:
        value1 = arr[low]

    if(high <= 0 or high >= len(arr)):
        value2 = float('inf')
    else:
        value2 = arr[high]

    # to find closest
    if abs(value1 - target) < abs(value2 - target):
        return value1
    else:
        return value2



def find_smallest_difference3(arr1, arr2):
    # base case
    if(len(arr1) == 0 or len(arr2) == 0):
        return -1
    
    if(len(arr1) > len(arr2)):
        find_smallest_difference3(arr2, arr1)
    
    arr1.sort()
    ans = float('inf')

    for target in arr2:
        closest = find_closest(arr1, target)
        diff = abs(closest - target)
        ans = min(ans, diff)

    return ans


arr1 = [1, 3, 5, 15, 11, 2]
arr2 = [23, 127, 235, 19, 8]

print(find_smallest_difference3(arr1, arr2))

# Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

# Example:
# arr = [1, 2, 3, 4], k=1
# 3 values differ by k=1: 2-1=1, 3-2=1, 4-3=1 --> output=3

# Constraints:
# 2 < len(arr) < 10^5
# 0 < k < 10^9
# 0 < arr[i] < 2^(31) - 1 



def pairs(arr, k):
    ans = 0
    
    # Approach 1: Binary search - For every no. in array, if it's target is present, ans += 1
    # Time Complexity: O(nlogn)
    arr.sort()
    for num in arr:
        target = num + k
        if binary_search(arr, target):
            ans += 1
    
    # Approach 2: Using set to save num and checking if it's complement is also present in the set
    # num_set = set()
    # for num in arr:
    #     num_set.add(num)
    # for num in num_set:
    #     if num + k in num_set:
    #         ans += 1

    
    # Approach 3: 2 pointer approach: Sort array and compare difference of elements with k
    arr.sort()
    start = 0
    end = 1
    
    while end < len(arr):
        diff = arr[end] - arr[start]
        if diff == k:
            ans += 1
            end += 1
        elif diff < k:
            end += 1
        else:
            start += 1

    return ans


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False



if __name__ == '__main__':
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = pairs(arr, k)
    print('Result=', result)
# An array arr has an inversion if index i < j but arr[i] > arr[j]
# Find the number of inversions in a given array

# Method 1:
# Brute Force: Check every value in nested loop
# Time Complexity = O(n^2), Space Complexity = O(1)
def count_inversions_simple(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                # inversion
                ans += 1
    return ans


# Method 2:
# Enhanced Merge Sort:
# Answer = no. of inversions in the right subarray + no. of inversions in the left subarray + no. of inversions in the merge() function
# To find the no. of inversions in merge(): Let i be used for indexing left subarray and j for right subarray. At any step in merge(), if a[i] is greater than a[j], then there are (mid – i) inversions. because left and right subarrays are sorted, so all the remaining elements in leftsubarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j] 

def mergeSort(arr, n):
    temp_arr = [0]*n    # to store sorted array in merge() function
    return _mergeSort(arr, temp_arr, 0, n-1)

def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr, left, mid)   # no. of inversions in left subarray
        inv_count += _mergeSort(arr, temp_arr, mid+1, right)    # no. of inversions in the right subarray
        inv_count += merge(arr, temp_arr, left, right, mid, inv_count) # no. of inversions in merge()
    return inv_count


def merge(arr, temp_arr, left, right, mid, inv_count):
    i = left    # starting index of the left subarray 
    j = mid + 1 # starting index of the right subarray
    k = left    # starting index of the sorted array

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # inversion
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            k += 1
            j += 1

    # Copy remaining elements of left subarray to temp_arr
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1 

    # Copy remaining elements of right subarray to temp_arr
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1 

    # Copy the sorted subarray into the original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count





if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print('Using Simple method:')
    print(count_inversions_simple(arr))
    print('Using Enhanced Merge Sort:')
    print(mergeSort(arr, len(arr)))

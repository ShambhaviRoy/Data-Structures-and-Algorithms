# n an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. 
# In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". 
# To correct an inversion, we can swap adjacent elements. Given an array arr, return the number of inversions to sort the array.

# Example: arr = [2, 4, 1]
# [2, 4, 1] --> [2, 1, 4] --> [1, 2, 4] (sorted)
# That is, swap(arr[1], arr[2]) and swap(arr[0], arr[1]) --> ans = 2


# Constraints:
# No. of test cases = t, 1 <= t <= 15
# len(arr) = n, 1 <= n <= 10^5
# 1 <= arr[i] <= 10^7



def countInversions(arr):
    n = len(arr)
    
    if n == 1:
        return 0
    
    n1 = n//2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    
    ans = countInversions(arr1) + countInversions(arr2)
    
    i1, i2 = 0, 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    
    return ans
    




if __name__ == '__main__':
    # No. of test cases
    t = int(input().strip())

    # Input for each test case
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        print(result)


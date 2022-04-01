# Find the number of contiguous subarrays in a sorted integer array
# Example: input arr = [0, 1, 2, 4, 5, 7]
# Output = 3 
# The contiguous subarrays are [0, 1, 2], [4, 5], [7]


# 2 pointer

def find_cont_subarrays(arr):
    n = len(arr)
    i, end = 0, 0

    ans = []
    subarray = []

    while i < n:
        end = i
        
        while end < n-1 and arr[end] + 1 == arr[end+1]:
            subarray.append(arr[end])
            end += 1
            
        ans.append(subarray)               
        i = end + 1

    return ans


if __name__ == '__main__':
    print('Enter length of arr:')
    n = int(input())
    arr = []

    print('Enter elements of arr:')
    for _ in range(n):
        arr.append(int(input()))

    ans = find_cont_subarrays(arr)
    print(ans)
    print(len(ans))
    
# Given an array arr of size n, its prefix sum array is another array prefixSum of the same size, such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i].

# Input  : arr = [10, 20, 10, 5, 15]
# Output : prefixSum = [10, 30, 40, 45, 60]


def find_prefix_sum_array(arr):
    prefix_sum = [0]*len(arr)

    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] += prefix_sum[i-1] + arr[i]

    return prefix_sum


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    answer = find_prefix_sum_array(arr)
    print('Original arr:', arr)
    print('Prefix Sum array:', answer)
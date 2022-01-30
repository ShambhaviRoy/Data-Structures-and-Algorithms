# We define the following:
# A subarray of array a of length n is a contiguous segment from a[i] through a[j] where 0 < i <= j <n .
# The sum of an array is the sum of its elements.
# Given an n element array of integers, a, and an integer, m, determine the maximum value of the sum of any of its subarrays modulo m.

from bisect import bisect, insort

def maximumSum(a, m):
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0

    for i in range(len(a)):
        sum_so_far = (sum_so_far + a[i]) % m    # maintaining a prefix sum array with modulo taken
        pos = bisect(cumulative_sums, sum_so_far)   # returns position just right of sum_so_far in cumulative_sums

        if pos == i:
            d = 0
        else:
            d = cumulative_sums[pos]

        max_sum = max(max_sum, (sum_so_far + m - d) % m)    # Since a%m = (a+m)%m

        insort(cumulative_sums, sum_so_far) # appending sum_so_far in cumulative_sums to maintain sorted order

    return max_sum



if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)
        print(result)

        
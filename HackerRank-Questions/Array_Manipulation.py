# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. 
# Once all operations have been performed, return the maximum value in the array.

# Example:
# n = 10
# queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]] --> m queries
# Queries are in the form a, b, k where a= start index, b = end index, k = increment
# Return max value once all queries are performed

# Constraints:
# 3 <= n <= 10^7
# 1 <= m <= *10^5
# 1 <= a, b <= n
# 0 <= k <= 10^9

def arrayManipulation(n, queries):
    # (n+2) as arr is 1-indexed, we only care about arr[1] to arr[n]
    arr = [0]*(n+2)
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
        print(arr)
    
    # calculate prefix sum --> retains maximum value needed
    maxnum = 0
    temp = 0
    for val in arr:
        temp += val
        maxnum = max(maxnum, temp)
    
    return maxnum

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)


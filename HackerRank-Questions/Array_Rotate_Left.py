# Rotate an array arr of length n by d steps
# Constraints:
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= a[i] <= 10^6

# Answer has d elements from front to the back and n-d elements from back to front

def rotLeft(a, n, d):
    alist = list(a)
    ans = a[d:] + a[0:d]
    return ans
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, n, d)
    print(result)


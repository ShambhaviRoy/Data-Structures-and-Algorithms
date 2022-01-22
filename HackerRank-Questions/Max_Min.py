# You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array arr'. Unfairness of an array is calculated as max(arr') - min(arr')


def maxMin(k, arr):
    arr.sort()     
    unfairness = max(arr) - min(arr)
    ans = 0
    start = 0
    end = k - 1
    
    while start < end and end < len(arr):
        ans = arr[end] - arr[start]
        if ans < unfairness:
            unfairness = ans 
        start += 1
        end += 1
    
    return unfairness 


if __name__ == '__main__':
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print('Result=', result)


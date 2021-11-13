# Consider an arbitrary integer x. Given an array of integers arr, 
# compute the running sum of x plus each integer in arr traveling from left to right through the array. 
# Restriction: running sum should be greater than 0
# Min possible value for x = ?

def brute_force(arr):
    x = 0
    while True:
        total = x
        is_valid = True
        for num in arr:
            total += num
            if total < 0:
                break
        if is_valid:
            return x
        else:
            x += 1


def binary_search(arr):
    m = 100
    n = len(arr)
    left = 1
    right = m*n + 1
    while left < right:
        middle = left + (right-left)//2
        total = middle
        for num in arr:
            total += num
            if total < 0:
                is_valid = False
                break
        if is_valid:
            right = middle
        else:
            left = middle + 1

    return left

def prefix_sum(arr):
    min_val = 0
    total = 0
    for num in arr:
        total += num
        min_val = min(min_val, total)
    return -min_val


if __name__ == '__main__':
    arr = [-3,2,-3,4,2]
    print(brute_force(arr))
    print(binary_search(arr))
    print(prefix_sum(arr))
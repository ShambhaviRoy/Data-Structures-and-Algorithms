# FInd largest integer whose square is less than equal to the given non-negative integer.

def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integer_square_root(300))
print(integer_square_root(12)) 
print(integer_square_root(1000))
print(integer_square_root(625))

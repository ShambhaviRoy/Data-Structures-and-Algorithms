import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# 1. bisect_left()- returns leftmost occurrence of target element
print(bisect.bisect_left(A, 108))
# -10 is at index 1
print(bisect.bisect_left(A, -10))
# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))

# 2. bisect_right()- returns index position after last occurrence 
# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10)) 
# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))

# 3. bisect()- same as bisect_right()
print(bisect.bisect(A, -10))
print(bisect.bisect(A, 285))
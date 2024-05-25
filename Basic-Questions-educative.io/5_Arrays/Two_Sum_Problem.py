#Given an array of integers, return True or False if the array has two numbers that add up to a specific target. 
# You may assume that each input would have exactly one solution.

#Solution 1: Brute Force Approach
#Make all pairs and check
#Time Complexity = O(n^2) and Space Complexity = O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A,target))
target = 20
print(two_sum_brute_force(A,target))


#Solution 2: Auxiliary Hash Table
#Time Complexity = O(n) and Space Complexity = O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_hash_table(A,target))


#Solution 3: 2 Indexes
#Time Complexity = O(n) and Space Complexity = O(1)
def two_sum(A, target):
    front = 0
    back = len(A) - 1
    while front < back:
        if A[front] + A[back] == target:
            print(A[front], A[back])
            return True
        elif A[front] + A[back] < target:
            front += 1
        else:
            back -= 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum(A,target))

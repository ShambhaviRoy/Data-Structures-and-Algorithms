# Given an array (nums) of integers, return an array with all of it's subsets 
# Example: Input = [1, 2, 3]
# Output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# https://leetcode.com/problems/subsets/

# Approach 1: Cascading
# Take an element from nums, it can/cannot be in subset
# Create all subsets and save it in an ans variable, and return ans
# Time Complexity = O(N * (2^N))
# Space Complexity = O(N * (2^N))

def cascading(nums):
    n = len(nums)
    ans = [[]]

    for num in nums:
        ans += [cur + [num] for cur in ans]

    return ans

# Approach 2: Backtracking
# Generate all possible subsets of length 0 to n
# Time Complexity = O(N * (2^N))
# Space Complexity = O(N) --> ans array is not counted, only cur is counted

def backtrack(first = 0, cur=[]):
    if len(cur) == k:
        ans.append(cur[:])
    for i in range(first, n):
        cur.append(nums[i])
        backtrack(i+1, cur)
        cur.pop()
    return ans
                
        

# Approach 3: Lexicographic (binary sorted) subsets
# Create bitmasks to have/not have a num in subset and map subsets to bitmasks
# For nums = [1, 2, 3], the subset [3] corresponds to bitmask '001'
# Generates lexicographically sorted output for sorted inputs and does not miss any subset
# Time Complexity = O(N * (2^N))
# Space Complexity = O(N * (2^N))

def subsets(nums):
    n = len(nums)
    ans = []
    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]
        ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    return ans






if __name__ == '__main__':
    print('Enter length of nums:')
    n = int(input())
    nums = []
    print('Enter elements of nums:')
    for _ in range(n):
        nums.append(int(input()))

    print(cascading(nums))

    ans = []
    for k in range(n+1):
        print(backtrack())

    print(subsets(nums))


    

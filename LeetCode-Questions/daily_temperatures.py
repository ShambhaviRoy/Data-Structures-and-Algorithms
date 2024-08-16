# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# https://leetcode.com/problems/daily-temperatures/description/

# Approach 1: 2 pointers
# Pointer i at current temperatures, j iterates through the rest of the array to find the next warmest day, ans = j - i
# Time Complexity = O(n^2)
# Space Complexity = O(1) excluding space for answer
def daily_temperatures1(temperatures):
    n = len(temperatures)
    ans = [0]*n
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if temperatures[i] < temperatures[j]:
                break
            j += 1
        if j == n:
            ans[i] = 0
        else:
            ans[i] = j-i
        i += 1
    return ans

# Approach 2: Use stack to store the index of warmest day so far
# Time Complexity = O(n)
# Space Complexity = O(n)
def daily_temperatures2(temperatures):
    n = len(temperatures)
    stack = []
    answer = [0]*n

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
    return answer
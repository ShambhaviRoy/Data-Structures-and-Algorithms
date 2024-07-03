# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150


# Approach 1: Using hash map
# Store the count of each each element in nums in a hash map
# For 2 fixed i and j, find whether complement = -(nums[i] + nums[j]) exists in hash map, and add to triplet
# Time Complexity = O(n^2)
# Space Complexity = O(n + m), n = len(nums), m = no. of triplets

def three_sum1(nums):
    n = len(nums)
    ans = set()
    triplet = set()
    num_map = {}
    
    for num in nums:
        if num not in num_map:
            num_map[num] = 1
        else:
            num_map[num] += 1

    for i in range(n-2):
        num_map[nums[i]] -= 1
        for j in range(i+1, n-1):
            num_map[nums[j]] -= 1
            complement = 0 - (nums[i] + nums[j])
            if complement in num_map and num_map[complement] > 0:
                triplet = tuple(sorted((nums[i], nums[j], complement)))
                ans.add(triplet)
            num_map[nums[j]] += 1
        num_map[nums[i]] += 1
            
    return ans


# Approach 2: Using 2 pointers
# Sort the array
# For fixed i, find j and k using 2 pointers (low and high)
# Time Complexity = O(n^2)
# Space Complexity = O(m), m = no. of triplets
def three_sum2(nums):
    n = len(nums)
    ans = []
    nums.sort()
    
    i = 0
    while i < n-2:
        if i == 0 or (i > 0 and nums[i] != nums[i-1]):
            low = i + 1
            high = n - 1

            while low < high:
                if nums[low] + nums[high] == -nums[i]:
                    triplet = [nums[i], nums[low], nums[high]]
                    ans.append(triplet)

                    # skipping over identical elements at low
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    # skipping over identical elements at high
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1

                elif nums[low] + nums[high] < -nums[i]:
                    low += 1
                
                else:
                    high -= 1
        i += 1

    return ans

                        



nums = [-1,0,1,2,-1,-4]
print(three_sum1(nums))
print(three_sum2(nums))

# Rotate an array of numbers (nums) by k positions (right shift)
# Constraints:
# 1 <= nums.length <= 10^5
# -2^(31) <= nums[i] <= 2^(31) - 1
# 0 <= k <= 10^5

def brute_force(nums, k):
    # Brute force
    n = len(nums)
    ans = [0]*n
    new_pos = 0
    num = 0

    for i in range(n):
        num = nums[i]
        new_pos = i + k
        if new_pos >= n:
            new_pos -= n
        ans[new_pos] = num
    
    return ans

# Using reverse
def using_reverse(nums, k):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    k %= len(nums)
    nums = reverse(nums, 0, len(nums)-1)
    nums = reverse(nums, 0, k-1)
    nums = reverse(nums, k, len(nums)-1)
    return nums




if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(brute_force(nums, k))
    print(using_reverse(nums, k))
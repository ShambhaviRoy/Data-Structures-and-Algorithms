# Given 2 arrays arr1 and arr2 and a target, find pairs of elements from the arrays adding up close to target
# The answer should be a tuple of elements from each array
# Example:
# arr1 = [-1, 3, 8, 2, 9, 5], arr2 = [4, 1, 2, 10, 5, 20], target = 24
# Answers = (3, 20) or (5, 20)

# Sort both arrays
# Maintain a matrix of sums: arr1 along y (increasing downwards), and arr2 along x (increasing rightwards)
# Start checking from top right corner:
# If sum > target: ignore that column and move left
# If sum < target: ignore that row and move down


def closest_pair(arr1, arr2, target):
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    i = 0
    j = len(arr2) - 1
    smallest_diff = abs(sorted_arr1[0] + sorted_arr2[0] - target)
    ans = (sorted_arr1[0], sorted_arr2[0])

    while i < len(sorted_arr1) and j >= 0:
        num1 = sorted_arr1[i]
        num2 = sorted_arr2[j]
        
        current_diff = num1 + num2 - target
        
        if abs(current_diff) < smallest_diff:
            smallest_diff = abs(current_diff)
            ans = (num1, num2)

        if current_diff == 0:
            return ans
        elif current_diff < 0:
            i += 1
        else:
            j -= 1

    return ans


arr1 = [-1, 3, 8, 2, 9, 5]
arr2 = [4, 1, 2, 10, 5, 20]
target = 24

print(closest_pair(arr1, arr2, target))
def find_closest_num(data, target):
    low = 0
    high = len(data) - 1
    min_diff = float('inf')
    closest_num = 0

    # Edge cases: The data is empty or the data has only 1 element
    if len(data) == 0:
        return None
    elif len(data) == 1:
        return data[0]

    while low < high:
        mid = (low + high) // 2

        # Ensure that you do not read beyond the bounds of the list
        if mid + 1 < len(data):
            min_diff_right = abs(data[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(data[mid - 1] - target)

        # Updata min_diff and closest_num
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid + 1]

        # Move mid as in binary search
        if target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
        else:
            return data[mid]
    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))
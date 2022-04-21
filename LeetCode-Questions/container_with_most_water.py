# https://leetcode.com/problems/container-with-most-water/


def max_area(height):
    ans = 0
    start = 0
    end = len(height)-1

    while start < end and end < len(height):
        area = min(height[start], height[end])*(end-start)
        ans = max(ans, area)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return ans


if __name__ == '__main__' :
    heights_len = int(input())
    heights = []
    for _ in range(heights_len):
        heights.append(int(input()))
    print(max_area(heights))

def get_max(nums, partition):
    if partition == 0:
        return -1e6
    else:
        return nums[partition-1]
            
            
def get_min(nums, partition):
    if partition == len(nums):
        return 1e6
    else:
        return nums[partition]


def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    low = 0
    high = len(nums1)
    combined_length = len(nums1) + len(nums2)
    
    while low <= high:
        part_x = (low + high)//2
        part_y = (combined_length + 1)//2 - part_x
        
        left_x = get_max(nums1, part_x)
        right_x = get_min(nums1, part_x)
        
        left_y = get_max(nums2, part_y)
        right_y = get_min(nums2, part_y)
        
        if left_x <= right_y and left_y <= right_x:
            if combined_length %2 == 0:
                return (max(left_x, left_y) + min(right_x, right_y))/2
            return max(left_x, left_y)
            
        
        if left_x > right_y:
            high = part_x - 1
        else:
            low = part_x + 1

    return -1


if __name__ == '__main__':
    print(findMedianSortedArrays(nums1 = [1, 3], nums2 = [2]))
    print(findMedianSortedArrays(nums1 = [1, 2], nums2 = [3, 4]))
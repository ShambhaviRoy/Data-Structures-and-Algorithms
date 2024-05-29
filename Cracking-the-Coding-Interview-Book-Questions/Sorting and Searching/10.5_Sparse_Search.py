# Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.
# EXAMPLE
# Input: ball, {'at', '', '', '', 'ball', '', '', 'cat', '', ''}
# Output: 4


def search(arr, target):
    if not arr or not target or target == '':
        return -1
    return search_string(arr, target, 0, len(arr)-1)
    

def search_string(arr, target, first, last):
    if first > last:
        return -1
    mid = (first + last)//2
    if arr[mid] == '':
        left = mid - 1
        right = mid - 1
        while(True):
            if left < first and right > last:
                return -1
            elif right <= last and arr[right] != '':
                mid = right
                break
            elif left >= first and arr[left] != '':
                mid = left
                break
            right += 1
            left -= 1

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        search_string(arr, target, first, mid - 1)
    else:
        search_string(arr, target, mid + 1, last)





arr = ['at', '', '', '', 'ball', '', '', 'cat', '', '']
target = 'ball'
print(search(arr, target))

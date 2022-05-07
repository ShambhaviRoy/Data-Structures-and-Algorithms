# Exponential Search
# The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. 
# Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)
# Given below are the implementations of above steps.

def binary_search(arr, x, low, high):
  if (low <= high):
    mid = low + (high-low)//2
    if arr[mid] == x:
      return mid
    elif x < arr[mid]:
      return binary_search(arr, x, low, mid-1)
    else:
      return binary_search(arr, x, mid+1, high)
  return -1


def exponential_search(arr, x, sub_size):
  if sub_size < len(arr):
    if arr[sub_size] == x:
      return sub_size
    if arr[sub_size] < x:
      return exponential_search(arr, x, sub_size*2)
    else:
      # binary search between sub_size//2 and sub_size
      low = sub_size // 2
      high = sub_size
      return binary_search(arr, x, low, high)
  return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 18

index = exponential_search(arr, x, 1)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponential_search(arr, x, 1)
if result == -1:
    print ("Element not found in the array")
else:
    print ("Element is present at index %d" %(result))
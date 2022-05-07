#interpolation search
#The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

def interpolation_search(arr, x, low, high):
  if (low <= high and x >= arr[low] and x <= arr[high]):
    pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))
    if x == arr[pos]:
      return pos
    if x < arr[pos]:
      return interpolation_search(arr, x, low, pos-1)
    if x > arr[pos]:
      return interpolation_search(arr, x, pos+1, high)
  
  return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 18

index = interpolation_search(arr, x, 0, n-1)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
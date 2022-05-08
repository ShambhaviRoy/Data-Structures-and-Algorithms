# Heap Sort

# Time Complexity: O(n log n)
# Since Heapify takes O(log n) and doing this for each element means O(n)


def heapify(arr, n, i):
    '''
    to heapify subtree rooted at index i
    n is the size of the heap
    '''
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        # swap
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



def heap_sort(arr):
    n = len(arr)

    # build a max-heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # replace root with last element of heap
    # then heapify this new root
    # do this till heap size > 1
    print('max heap arr:', arr)
    print('--'*20)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print('i=', i)
        print('before heapify:', arr)
        heapify(arr, i, 0)
        print('after heapify:', arr)
        print('-'*20)


arr = [4, 10, 3, 5, 1]
print('Input array:', arr)
heap_sort(arr)
print("Sorted array:", arr)
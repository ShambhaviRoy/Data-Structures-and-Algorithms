# Question: Given two sorted arrays, find the number of elements in common. The arrays are the same length and each has all distinct elements.

# Example: 
# arr1 = [10, 13, 15, 23, 45, 67]
# arr2 = [13, 23, 33, 67, 71, 89]
# The common elements in arr1 and arr2 are [13, 23, 67] --> ans = 3

# Approach:
# Search each element of arr1 in arr2. That would take O(n^2) time. 
# Since these arrays are sorted, we could use binary search and this would take O(n log n) time.
# Look for an element from arr1 in arr2, if we encounter an element greater, then we stop looking further. And this way, each search starts where the previous one ended.
# So this is linear search and would take O(n) time.

# Time complexity = O(n)
# Space complexity = O(1)


def find_common_elements(arr1, arr2):
    n = len(arr1)
    min_pos = 0
    max_pos = 1
    ans = 0

    for i in range(n):
        element = arr1[i]
        # search for this element in arr2 (linear search)  
        while(max_pos < n):
            subarr2 = arr2[min_pos : max_pos+1]
            # if element < arr2[min_pos]:
            #     # lower than min
            #     continue
            if element > arr2[max_pos]:
                # greater than max
                min_pos = max_pos
                max_pos += 1
            else:
                # element within subarr2
                if element in subarr2:
                    ans += 1
                    min_pos = max_pos
                    max_pos += 1 

    print('Answer = ', ans)




if __name__ == "__main__":
    # print("Enter no. of elements in both arrays")
    # n = int(input())
    # arr1 = [0]*n
    # arr2 = [0]*n
    
    # print("Enter elements of arr1 one-by-one")
    # for i in range(n):
    #     arr1[i] = int(input())

    # print("Enter elements of arr2 one-by-one")
    # for i in range(n):
    #     arr2[i] = int(input())

    arr1 = [10, 13, 15, 23, 45, 67]
    arr2 = [13, 23, 33, 67, 71, 89]

    find_common_elements(arr1, arr2)



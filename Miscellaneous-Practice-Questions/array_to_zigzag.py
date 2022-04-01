# Convert an array to zig-zag fashion
# That is, for any given array arr = [a, b, c, d, e], it is zig-zag if a<b>c<d>e

# Time Complexity = O(n)

def convert_arr(arr):
    # flag = True shows there should be '<' relationship between arr[i] and arr[i+1]
    flag = True

    for i in range(len(arr) - 1):
        if flag is True:
            # there should be '<' relationship
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            # there should be '>' relationship
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        # switch flag
        flag = bool(1-flag)

    return arr



if __name__ == '__main__':
    print('Enter length of arr:')
    n = int(input())
    arr = []

    print('Enter elements of arr:')
    for _ in range(n):
        arr.append(int(input()))

    ans = convert_arr(arr)
    print(ans)

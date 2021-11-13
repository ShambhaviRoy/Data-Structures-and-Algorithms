# Given array A = [-1, 1, 2, 3, -5, 6]
# Sorted A = [-5, -1, 1, 2, 3, 6]
# Zigzag array = [6, -5, 3, -1, 2, 1]


def zigzag_array(A):
    answer = []
    A.sort()

    start = 0
    end = len(A) - 1

    while start <= end:
        if start == end:
            answer.append(A[start])
        else:
            answer.append(A[end])
            answer.append(A[start])
        start += 1
        end -= 1
    return answer


if __name__ == '__main__':
    # odd length
    A1 = [-1, 1, 2, 3, -5, 6]
    print(zigzag_array(A1))
    # even length
    A2 = [-1, 1, 2, 3, -5]
    print(zigzag_array(A2))
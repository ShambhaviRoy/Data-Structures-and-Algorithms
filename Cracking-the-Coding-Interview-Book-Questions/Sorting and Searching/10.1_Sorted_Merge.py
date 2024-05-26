# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

def merge_sorted(A, B):
    return merge(A, B, 5, 4)

def merge(A, B, lastA, lastB):
    indexA = lastA - 1
    indexB = lastB - 1
    indexMerged = lastA + lastB - 1
    while indexB >= 0:
        if indexA >= 0 and A[indexA] > B[indexB]:
            A[indexMerged] = A[indexA]
            indexA -= 1
        else:
            A[indexMerged] = B[indexB]
            indexB -= 1
        indexMerged -= 1
    return A


    


A = [2, 4, 6, 8, 10, 0, 0, 0, 0]
B = [1, 2, 3, 5]
print(merge_sorted(A, B))
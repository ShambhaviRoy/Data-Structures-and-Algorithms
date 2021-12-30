#Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A).intersection(B))

def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []
    #traverse arrays
    while i < len(A) and j < len(B):
            #intersecting element found
            if A[i] == B[j]:
                return True
                if i == 0 or A[i] != A[i - 1]:  #check duplicates
                    intersection.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
    return intersection
    

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))
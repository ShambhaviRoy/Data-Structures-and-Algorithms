# 1570. Dot Product of Two Sparse Vectors
# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

# nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# answer = 0 + 0 + 0 + 8 + 0 = 8
# vec1 = {0: 1, 3: 2, 4: 3}, vec2 = {1: 3, 3: 4}

class SparseVector:
    def __init__(self, nums):
        self.vector = {}
        self.length = len(nums)
        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num

    def dotProduct(self, vec):
        # both vectors are sparse
        vector1 = self.vector
        vector2 = SparseVector(vec).vector
        ans = 0
        for i in range(self.length):
            if i in vector1 and i in vector2:
                ans += vector1[i] * vector2[i]
        return ans
    
    def dotProduct2(self, vec):
        # Follow up: if only one of the vectors is sparse
        ans = 0
        for i, num in self.vector.items():
            ans += num * vec[i]
        return ans


    

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
print(v1.dotProduct(nums2))
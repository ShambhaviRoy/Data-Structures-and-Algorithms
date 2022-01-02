# Target Sum Subsets
# https://nados.pepcoding.com/content/eb9863ac-63ac-4b94-881f-0aeb24df0985/0c54b191-7b99-4f2c-acb3-e7f2ec748b2a/ae41ae29-11ca-4ae4-8ec7-72a411fd59b6/d341a7c9-1269-409c-b851-0bb512289544/9c432afc-f3ff-4c3c-95a5-f2aca5ecfc1a/question/99046367-231c-4847-8579-3d85ac55501a

# 1. You are given a number n, representing the count of elements.
# 2. You are given n numbers.
# 3. You are given a number "tar".
# 4. Complete the body of printTargetSumSubsets function - without changing signature - to calculate and print all subsets of given elements, the contents of which sum to "tar". 


# asf is the subset
# sos is sum of subset
# tar is target
def printTargetSumSubsets(arr, idx, asf, sos, tar):
    if sos > tar:
        return

    if idx == len(arr):
        if sos == tar:
            print(asf + '.')
        return

    printTargetSumSubsets(arr, idx+1, asf+str(arr[idx])+', ', sos+arr[idx], tar)
    printTargetSumSubsets(arr, idx+1, asf, sos, tar)


   


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    
    tar = int(input())
    printTargetSumSubsets(arr, 0, '', 0, tar)


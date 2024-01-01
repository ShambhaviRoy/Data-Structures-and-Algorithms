# You are given two 32-bit numbers, Nand M, and two bit positions, i and j. Write a method
# to insert Minto N such that M starts at bit j and ends at bit i. You can assume that the bits j through
# i have enough space to fit all of M. That is, if M = 18811, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
# fit between bit 3 and bit 2.


def insertion(N, M, i, j):
    # create mask
    all_ones = ~0
    left = all_ones << (j+1)
    right = (1 << i)-1
    mask = left | right

    # clear bits i through j in N using the mask
    N_cleared = N & mask

    # shift M to align with bit positions i and j
    M_shifted = M << i

    return N_cleared | M_shifted


N = 1024 #10000000000
M = 19 #10011
i = 2
j = 6
print(insertion(N, M, i, j))
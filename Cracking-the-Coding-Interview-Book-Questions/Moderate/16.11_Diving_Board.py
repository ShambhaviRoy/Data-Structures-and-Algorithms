# Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
# There are two types of planks, one of length shorter and one of length longer. You must use
# exactly K planks of wood. Write a method to generate all possible lengths for the diving board.

# Time complexity = O(n)

def find_all_lengths(K, shorter, longer):
    lengths = []
    for n in range(0, K+1):
        length1 = n * shorter + (K-n) * longer
        lengths.append(length1)
    return lengths


def print_lengths(lengths):
    print(len(lengths))
    print(lengths)
    for length in lengths:
        print(length)


lengths = find_all_lengths(6, 2, 3)
print_lengths(lengths)

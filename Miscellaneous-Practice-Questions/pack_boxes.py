# You are given array of integers called blocks. Each of the values in this array represents the width of a block - the ith block has a height of 1 and a width of blocks[i] (i.e. it's a 1 x blocks[i] block).

# You want to pack all the given blocks into a rectangular container of dimensions height x width, according to the following rules:

# Place blocks into the container row by row, starting with block 0.
# For each row, place the blocks into the container one by one, in the order they are given in the blocks array.
# If there is not enough space to put the current block in the current row, start filling the next row.
# You are given the value height of the rectangular container. Your task is to find the minimal possible width of a rectangular container in which all blocks can fit. Find and return this minimal possible width value.

# Note: The blocks cannot be rotated.
# For blocks = [1, 3, 1, 3, 3] and height = 2, the output should be solution(blocks, height) = 6.
# Note that it wouldn't be possible to fit these blocks in a container that's any less wide than 6.
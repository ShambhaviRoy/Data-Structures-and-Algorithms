# Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).



def swap_odd_even_bits(x):
    odd_shifted = (x & 0xaaaaaa) >> 1   # move odd bits by 1 to even places
    even_shifted = (x & 0x55555) << 1   # move even bits by 1 to odd places
    return odd_shifted | even_shifted   # bitwise OR



print(swap_odd_even_bits(45))
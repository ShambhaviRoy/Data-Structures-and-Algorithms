# Basic bit operations

# get ith bit
def get_bit(num, i):
    return (num & (1 << i) != 0)


# set ith bit
def set_bit(num, i):
    return num | (1 << i)


# clear ith bit
def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask 


# clear MSB through ith bit inclusive
def clear_MSB_through_i_bits(num, i):
    mask = (1 << i) - 1
    return num & mask


# clear ith bit through LSB
def clear_i_through_LSB_bits(num, i):
    mask = (-1 << (i+1))
    return num & mask 


# update ith bit
def update_bit(num, i, bitIs1):
    v = 1 if bitIs1 else 0
    mask = ~(1 << i)
    return (num & mask) | (v << i)


print(get_bit(27, 3))
print(set_bit(27, 3))
print(clear_bit(27, 3))
print(clear_MSB_through_i_bits(27, 3))
print(update_bit(4, 1, True))
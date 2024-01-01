# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.

def flip_bit(num):
    if (~num == 0):
        return (1 << 8)-1
    
    curr1slen = 0
    prev1slen = 0
    max1slen = 1

    while(num != 0):
        if((num & 1) == 1):
            curr1slen += 1
        elif ((num & 1) == 0):
            prev1slen = 0 if (num & 2) == 0 else curr1slen
            curr1slen = 0
        
        max1slen = max(prev1slen + curr1slen + 1, max1slen)
        num = num >> 1

    return max1slen



print(flip_bit(1775))

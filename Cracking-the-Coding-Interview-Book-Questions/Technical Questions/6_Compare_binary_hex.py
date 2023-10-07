# write a function to check if the value of a binary number (passed as a string)
# equals the hexadecimal representation of a string

def compare_bin_to_hex(binary, hex):
    n1 = convert_to_int(binary, 2)
    n2 = convert_to_int(hex, 16)
    print(n1 == n2)


def convert_to_int(number, base):
    if (base < 2 or (base > 10 and base != 16)):
        return -1
    n = 0
    index = 0
    for d in reversed(number):
        n += int(d) * (base**index)
        index += 1
    return n



compare_bin_to_hex("1001", "9")
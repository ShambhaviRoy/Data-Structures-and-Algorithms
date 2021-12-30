from Stack_data_structure import Stack

def convert_int_to_bin(dec_num):
    #edge case: dec_num = 0
    if dec_num == 0:
        return 0
    
    s = Stack()
    
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num

print(convert_int_to_bin(242))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))


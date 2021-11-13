# 123 --> '123' and -123 --> '-123'
# ord('0') = 48 --> unicode of character '0' is 48
# chr(48) = '0'  --> outputs character on unicode input
 

def int_to_string(input_int):
    
    # If given integer is negative
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10) )
        input_int = input_int - (input_int % 10)

    output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str

    
print(int_to_string(123))
print(int_to_string(-123))
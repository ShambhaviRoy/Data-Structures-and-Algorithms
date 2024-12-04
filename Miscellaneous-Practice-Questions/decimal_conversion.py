# Decimal Conversion
# Given a numerator and denominator, calculate fraction and represent in string form
# Examples
# decimal_conversion(9, 2) = "4.5"
# decimal_conversion(-15, 3) = "-5.0"
# decimal_conversion(1, 3) = "0.(3)"


def decimal_conversion(numerator, denominator):
    # edge cases
    if numerator == 0:
        return 0
    if denominator == 0:
        return "NaN"
    
    integer = int(numerator / denominator)
    remainder = numerator % denominator

    if remainder == 0:
        return str(integer) + '.' + '0'

    answer = str(integer) + '.'

    fractional_part = []
    remainder_positions = {}

    while remainder != 0:
        if remainder in remainder_positions:
            repeat_start = remainder_positions[remainder]
            non_repeating = ''.join(fractional_part[:repeat_start])
            repeating = ''.join(fractional_part[repeat_start:])
            return answer + non_repeating + '(' + repeating + ')'

        remainder_positions[remainder] = len(fractional_part)
        remainder = remainder * 10
        fractional_part.append(str(remainder // denominator))
        remainder = remainder % denominator
        
    return answer + ''.join(fractional_part)
    

print(decimal_conversion(9, 2))
print(decimal_conversion(-15, 3))
print(decimal_conversion(1, 3))
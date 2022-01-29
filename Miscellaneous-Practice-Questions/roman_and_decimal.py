# Functions to convert a roman numeral to decimal and decimal number to roman

# Translations:
# translations = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}

# A number in Roman Numerals is a string of these symbols written in descending order(e.g. M’s first, followed by D’s, etc.). However, in a few specific cases, to avoid four characters being repeated in succession(such as IIII or XXXX), subtractive notation is often used, subtracting value of symbol from next symbol
# Examples: 'III' --> 3, 'VIII' --> 8, 'IX' --> 9, 'XL' --> 40


# Roman --> Decimal
# Traverse the roman numeral (all except last symbol), check the translation of left and right symbols for additive or subtractive conditions and keep adding to running total
# Then add the value of the last (final) roman symbol

# Time Complexity = O(n), Space Complexity = O(n)

def roman_to_decimal(roman):
    decimal_ans = 0
    translations = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
    
    for i in range(len(roman)-1):
        left = roman[i]
        right = roman[i+1]

        if translations[left] < translations[right]:    
            decimal_ans -= translations[left]   # subtracting value of left
        else:
            decimal_ans += translations[left]   # adding value of left

    decimal_ans += translations[roman[-1]]  # adding value of last symbol
    return decimal_ans


# Decimal --> Roman
# The given decimal no. is compared with bases to find the largest base smaller than the given decimal no. Dividing the decimal no. by this largest base, the corresponding symbol is repeated quotient times
# Update decimal number by subtracting the base from the decimal no. and continue this till the decimal no. becomes 0.

# Time Complexity = O(n), Space Complexity = O(n)

def decimal_to_roman(decimal):
    roman_ans = ''

    bases = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = 12  # length of bases list

    while decimal:
        div = decimal // bases[i]
        decimal %= bases[i]
        roman_ans += symbols[i]*div
        i -= 1

    return roman_ans




if __name__ == '__main__':
    roman_ip = input()
    decimal_ans = roman_to_decimal(roman_ip)
    print(decimal_ans)

    decimal_ip = int(input())
    roman_ans = decimal_to_roman(decimal_ip)
    print(roman_ans)

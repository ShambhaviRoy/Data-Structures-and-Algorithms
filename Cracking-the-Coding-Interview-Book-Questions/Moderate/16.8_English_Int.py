# English Int: Given any integer, print an English phrase that describes the integer (e.g., "One Thousand,
# Two Hundred Thirty Four").

digits_map = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5: 'Five',
              6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine'}

places_map = {1000 : 'Thousand', 100 : 'Hundred'}

tens_map = {10 : 'Ten', 20 : 'Twenty', 30 : 'Thirty', 40: 'Forty', 50 : 'Fifty',
            60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety'}



def count_digits(num):
    digits = 0
    while(num >= 1):
        digits += 1
        num = num / 10
    return digits


def english_to_int(num):
    ans = ""
    
    while(num > 0):
        print(num)
        digits = count_digits(num)
        divisor = 10 ** (digits - 1)
        d = num // divisor
        unit = num % divisor
        if(num < 100):
            ans += tens_map[d * divisor] + ' ' + digits_map[unit]
            num = 0
        else:
            ans += digits_map[d] + ' ' + places_map[divisor] + ' '
            num = num % divisor

    if(num < 0):
        ans += 'Negative ' + english_to_int(-1 * num)
        
    return ans
        



print(english_to_int(1234))
print(english_to_int(-123))
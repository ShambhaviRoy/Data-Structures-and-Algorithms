# Shift string by a certain rotation_factor
# Example:
# input = Zebra-493?
# rotationFactor = 3
# output = Cheud-726?
# Constraints:
# 1 <= |input| <= 1,000,000
# 0 <= rotation_factor <= 1,000,000


import math

def rotationalCipher(input, rotation_factor):
  ans = ''
  
  if rotation_factor == 0:
    return input
  
  for ch in input:
    unicode = ord(ch)
    
    if ch.isalpha() or ch.isnumeric():
      # uppercase alphabet
      if unicode in range(65, 91):
        new_unicode = ((unicode - ord('A') + rotation_factor) % 26) + ord('A')

      # lowercase alphabet
      elif unicode in range(97, 123):
        new_unicode = ((unicode - ord('a') + rotation_factor) % 26) + ord('a')

      # digit
      else:
        new_unicode = ((unicode - ord('0') + rotation_factor) % 10) + ord('0')
    
    # special characters
    else:
      new_unicode = unicode
    
    ans += chr(new_unicode)

  return ans


if __name__ == '__main__':
    input_str = input()
    rotation_factor = int(input())
    print(rotationalCipher(input_str, rotation_factor)) 

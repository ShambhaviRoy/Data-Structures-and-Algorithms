# Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at
# most 32 characters, print "ERROR:'


def binary_to_string(num):
    if num >= 1:
        return 'ERROR'
    
    ans = '.'

    while(num > 0):
        r = 2 * num
        if(r >= 1):
            num = r - 1
            ans += '1'
        else:
            num = r
            ans += '0'

    return ans
            

print(binary_to_string(0.72))
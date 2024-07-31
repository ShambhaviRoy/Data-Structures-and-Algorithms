# Write a program to determine whether an input string x is a substring of another input string y
# (For example, "bat" is a substring of "abate", but not of "beat".)

def is_substring(x, y):
    x_ptr = 0
    y_ptr = 0

    while(x_ptr < len(x) and y_ptr < len(y)):
        if x[x_ptr] != y[y_ptr]:
            y_ptr += 1
        else:
            y_ptr = x_ptr
            while(y_ptr < len(y)):
                if y[y_ptr] == x[x_ptr]:
                    x_ptr += 1
                    y_ptr += 1
                else:
                    return False
        return True
    

x = 'bat'
y = 'abate'
print(is_substring(x, y) == True)

y = 'beat'
print(is_substring(x, y) == False)
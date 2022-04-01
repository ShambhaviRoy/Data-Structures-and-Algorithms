# Given a mathematical expression in string with only addition and multiplication, calculate it's value (return int)
# Example inputs:
# '4*4*4'
# '23*45'
# '23*45 + 2*72'

# Time Complexity = O(n)
# Space Complexity = O(1)

def eval(s):
    ans = 0
    l1 = s.split('+')
    for st in l1:
        product = 1
        l2 = st.split('*')
        for num in l2:
            product *= int(num)
        ans += product
    return ans


if __name__ == '__main__':
    print('Enter expression:')
    s = input()
    print(eval(s))
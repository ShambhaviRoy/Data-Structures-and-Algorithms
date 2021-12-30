# Find GCD and LCM of 2 numbers n1 and n2
# GCD --> repeated division
# LCM --> (n1*n2)//gcd


def gcdandlcm(n1,n2):
    # write your code here
    divisor = n1
    dividend = n2

    while dividend % divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    gcd = divisor
    lcm = (n1 * n2)//gcd 

    print(gcd)
    print(lcm)

def main():
    n1 = int(input())
    n2 = int(input())
    gcdandlcm(n1,n2)

if __name__=="__main__":
    main()

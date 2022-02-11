# Given a number, find the number of 1's in it's binary representation
# Example: 5 --> '101' --> Output = 2

# Not finding the binary representation of the number


def find_ones(num):
    ans = 0
    while num > 0:
        rem = num % 2
        if rem == 1:
            ans += 1
        num = num // 2
    return ans


if __name__ == '__main__':
    num = int(input())
    print(find_ones(num))



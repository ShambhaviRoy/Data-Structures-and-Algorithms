# Write a function hanoi(n, start, end) that outputs a sequence of steps to move n discs from the start rod to the end rod
# Assumptions: 
# 0 < n < 9
# 1 <= start, end <= 3
# start != end

# Using a helper function print_move to show that the top disc is moved from a start rod to an end rod: 
# print_move(start, end) = print(start, -->, end)

# hanoi(n, start, end) = print_move(start, end) if n = 1
                    # = other = 6 - (start + end) --> reference to other rod, except start and end
                    # hanoi(n-1, start, other) --> Move n-1 discs from the start rod to other rod
                    # print_move(start, end) --> Move the largest disc (last remaining) on start rod to the end rod
                    # hanoi(n-1, other, end) --> Move the n-1 discs from the other rod to the end rod


def hanoi(n, start, end):
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        print_move(start, end)
        hanoi(n-1, other, end)


def print_move(start, end):
    print(str(start) + '-->' + str(end))


if __name__ == "__main__":
    # Towers of Hanoi problem to move 3 discs from rod 1 to rod 3
    hanoi(3, 1, 3) 


# You're given an unsorted array of integers where every integer appears exactly 
# twice, except for one integer which appears only once.  Write an algorithm that finds the integer that appears only once.

# Approach 1: Set to keep unique no.s and a total of all numbers, if no. seen again, subtract from total, this will leave the no. added only once
# Time Complexity = O(n)
# Space Complexity = O(n)
def odd_man_out(array):
    numbers = set()
    total = 0
    for num in array:
        if num not in numbers:
            numbers.add(num)
            total += num
        else:
            total -= num
    return total

# Approach 2: XOR all numbers
# Time Complexity = O(n)
# Space Complexity = O(1)
def odd_man_out2(array):
    total = 0
    for num in array:
        total ^= num
    return total


array = [1, 3, 2, 4, 5, 4, 3 , 2, 5]
print(odd_man_out(array))
print(odd_man_out2(array))
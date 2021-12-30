st = "LucidProgramming"
print(len(st))

def find_length_iterative(input_str):
    count = 0
    for ch in input_str:
        count = count + 1
    return count

def find_length_recursive(input_str, count = 0):
    # base case: if input_str is an empty string
    if input_str == '':
        return 0
    return 1 + find_length_recursive(input_str[1:])

print(find_length_iterative(st))
print(find_length_recursive(st))
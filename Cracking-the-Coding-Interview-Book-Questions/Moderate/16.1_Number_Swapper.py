# Number Swapper: Write a function to swap a number in place (that is, without temporary variables).

def swap_numbers(num1, num2):
    num1 = num1 - num2  # num1 = 9-4 = 5
    num2 = num1 + num2  # num2 = 5+4 = 9
    num1 = num2 - num1  # num1 = 9-5 = 4
    
    print("num1 = ", num1)
    print("num2 = ", num2)



num1 = 9
num2 = 4
print("Given num1 = ", num1, " num2 = ", num2)
swap_numbers(num1, num2)
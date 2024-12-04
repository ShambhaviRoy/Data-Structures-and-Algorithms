# Check if an integer is a power of 10

def is_power_of_10(n):
    if n == 1:
        return True
    if n % 10 != 0:
        return False
    return is_power_of_10(n/10)

print(is_power_of_10(10000))
print(is_power_of_10(30))
print(is_power_of_10(25))
# Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.



def make_change(n):
    if n < 0:
        return 
    if n == 0:
        return '0p'
    
    if n >= 1 and n < 5:
        return [str(n) + 'p']
    
    if n >= 5 and n<10:
        nickels = find_coins(n, 5)
        remaining = n - nickels*5
        return [str(nickels) + 'n' + way for way in ways]
    
    
    all_ways = []

    quarters = find_coins(n, 25)

    while(quarters >= 0):
        
        remaining = n - quarters*25
        dimes = find_coins(remaining, 10)
        remaining -= dimes*10
        nickels = find_coins(remaining, 5)
        remaining -= nickels*5
        ways = make_change(remaining)

        for way in ways:
            way += str(quarters) + 'q' + str(dimes) + 'd' + str(nickels) + 'n'
            all_ways.append(way)
        quarters -= 1

    return all_ways


def find_coins(n, denomination):
    return n//denomination

        

n = 103
print(len(make_change(n)))
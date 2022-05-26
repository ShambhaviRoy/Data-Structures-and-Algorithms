# Given a value V, if we want to make a change for Rs. V, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change?

# Example 1: 
# V = 70, output = 2
# As we need 1 Rs. 50 coin and 1 Rs. 20 coin

# Example 2:
# V = 121, output = 3
# As we need 1 Rs. 100 coin, 1 Rs. 20 coin and 1 Rs. 1 coin

# Time Complexity = O(V), Space Complexity = O(V)

def minimum_coins(V):
    ans = 0
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]   # denominations of coins
    change = [] # list to store the coins required for V

    for coin in reversed(coins):
        while V / coin >= 1:
            V = V - coin
            ans += 1
            change.append(coin)

    return ans, change



V = int(input())
print(minimum_coins(V))
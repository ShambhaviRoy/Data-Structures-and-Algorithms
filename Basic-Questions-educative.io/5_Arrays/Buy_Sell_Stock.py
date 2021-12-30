#Solution 1: Brute Force
#Time Complexity = O(n^2) and Space Complexity = O(1)
def buy_and_sell_stock_1(A):
  max_profit = 0

  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
        max_profit = A[j] - A[i]
  return max_profit


#Solution 2: Tracking min price
#Time Complexity = O(n)
def buy_and_sell_stock_2(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price) 
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit



A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_1(A))
print(buy_and_sell_stock_2(A))
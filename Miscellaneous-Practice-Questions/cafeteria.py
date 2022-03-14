# A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.
# There are currently M diners seated at the table, the ith of whom is in seat S_i
# No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
# Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
# Please take care to write a solution which runs within the time limit.
# Constraints
# 1 <= N <= 10^{15}
# 1 <= K <= N
# 1 <= M <= 500,000
# M < N
# 1 <= S_i <= N

# Example: 
# N = 10, K = 1, M = 2, S = [2, 6]
# Ans = 3
# Seats: 1 2 3 4 5 6 7 8 9 10
# 1-2-3, 4-5-6 occupied or can't be used --> count the remaining = 3 (ans)


def getMaxAdditionalDinersCount(N, K, M, S):
  # Write your code here
  ans = 0
  print(list(range(1, N+1)))
  # 0 means unoccupied
  seats = [0 for _ in range(1, N+1)]
  print(seats)

  # fill up seats in S --> occupied already or can't be occupied
  for s in S:
    seat = s-K
    while seat < s+K+1:
          seats[seat-1] = 1
          seat += 1
    print(seats)

  return seats.count(0)





if __name__ == '__main__':
    N = int(input())
    K = int(input())
    M = int(input())
    S = []
    for _ in range(M):
        S.append(int(input()))
    print(getMaxAdditionalDinersCount(N, K, M, S))

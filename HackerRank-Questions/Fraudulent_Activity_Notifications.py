# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2* the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all  days.

# n = number of days of transaction data
# d = number of days to consider trailing data

# Constraints:
# 1 <= n <= 2*10^5
# 1 <= d <= n
# 0 < expenditure[i] <= 200

#!/bin/python3

import math
import os
import random
import re
import sys


def activityNotifications(expenditure, d):
    lookback = {}
    
    # to get median
    def get_median(idx):
        s = 0
        for i in range(201):
            freq = 0
            if i in lookback:
                freq = lookback[i]
            s += freq
            
            if s >= idx:
                return i
            
    ans = 0
    
    for i in range(n):
        val = expenditure[i]
        
        if i >= d: # we have a lookback window
            med = get_median(d//2 + d%2)
            
            if d % 2 == 0:
                if val >= med + get_median(d//2 + 1):
                    ans += 1
            else:
                if val >= 2*med:
                    ans += 1
        
        # add current value in lookback 
        if val not in lookback:
            lookback[val] = 1
        else:
            lookback[val] += 1
            
        # remove previous element from lookback
        if i >= d:
            prev = expenditure[i-d]
            lookback[prev] -= 1
            
    return ans
                    
                    
                
                 
    
    
                

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)

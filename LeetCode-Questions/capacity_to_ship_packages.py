# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# Approach:
# We need to find the right capacity- the minimum capacity will be the maximum weight and the maximum capacity will be the sum of all weights
# So we can use binary search to check capacity
# We have to check whether we can add weights without exceeding capacity, keeping track of the days needed

def check(weights, capacity, days):
    days_used = 0
    capacity_used = capacity
    
    for weight in weights:
        if capacity_used + weight > capacity:
            days_used += 1
            capacity_used = 0
        capacity_used += weight

    return days_used <= days



def ship_packages_within_days(weights, days):
    min_capacity = max(weights)
    max_capacity = sum(weights)

    capacity = min_capacity

    while min_capacity <= max_capacity:
        capacity = (min_capacity + max_capacity)//2
        if check(weights, capacity, days):
            min_capacity = capacity
            max_capacity -= 1
        else:
            min_capacity += 1
    return capacity


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(ship_packages_within_days(weights, days))


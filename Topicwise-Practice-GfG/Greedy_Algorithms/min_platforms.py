# Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. 
# We are given two arrays that represent the arrival and departure times of trains that stop.

# Approach 1: Naive
# Find the no. of overlapping intervals with each interval and return the maximum no. of overlaps

# Time Complexity = O(n^2)

def max_platforms_naive(arr, dep):
    n = len(arr)
    ans = 0
     
    for i in range(n):
        overlaps = 1
        for j in range(i+1, n):
            if max(arr[i], arr[j]) <= min(dep[i], dep[j]):
                overlaps += 1
        
        ans = max(overlaps, ans)

    return ans


# Approach 2: Greedy
# Create an array to store arrival and departure times and sort it based on arrival times
# Keep track of last departure time in a queue, ans = 0
# If arrival time of current train is before departure time of previous train, there is overlap --> push current departure time to queue and increment ans
# Else pop the departure time
# Push the current departure time to queue
# Finally return ans

# Time Complexity = O(n log n), Space Complexity = O(n)

def max_platforms_greedy(arr, dep):
    times = []

    for at, dt in zip(arr, dep):
        times.append((at, dt))

    times.sort(key = lambda x: x[0])    # sorted times based on arrival time

    queue = [times[0][1]]   # departure time of 1st train
    ans = 0

    for i in range(1, len(times)):
        t = queue[-1]
        if times[i][0] <= t:
            queue.append(times[i][1])
            ans += 1
        else:
            queue.pop(0)
        queue.append(times[i][1])

    return ans


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(max_platforms_naive(arr, dep))

print(max_platforms_greedy(arr, dep))



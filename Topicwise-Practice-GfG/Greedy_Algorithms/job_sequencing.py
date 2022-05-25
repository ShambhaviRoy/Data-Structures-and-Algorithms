# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time?

# Approach 1: Greedy Algorithm
# Time Complexity = O(n^2)

def job_sequencing(arr, t):
    # sort the jobs in decreasing order of Profit
    arr.sort(key = lambda x: x[2], reverse = True)

    result = [False]*t
    jobs = ['']*t

    for i in range(len(arr)):
        job_row = arr[i]
        for j in range(min(t-1, job_row[1] - 1), -1, -1):
            if result[j] == False:
                result[j] = True
                jobs[j] = job_row[0]
                break

    return jobs

# Job Array (JobID, Deadline, Profit)
arr = [['a', 2, 100],  
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
t = 3   # no. of jobs in sequence 

print(job_sequencing(arr, t))
# A company has psychometric tests for n candidates and it will only extend job offers to candidates with scores in the range [lowerLimit, upperLimit].
# Given a list of scores and a sequence of score ranges, determine how many candidates the company will extend offers to for each range of scores.



# Approach 1: Comparing each score with each upper and lower limit
# Time Complexity = O(n^2)
from ast import Pass


def job_offers1(candidate_scores, lower_limits, upper_limits):
    jobs_list = []

    for i in range(len(lower_limits)):
        candidates = 0
        # if candidate score is within lower_limits[i] and upper_limits[i], the candidate has passed
        for score in candidate_scores:
            if score >= lower_limits[i] and score <= upper_limits[i]:
                candidates += 1
        jobs_list.append(candidates)

    return jobs_list


# Approach 2: Sort the scores, find the number of scores (indices) within limits

# to find the first index >= x
def lower_index(arr, n, x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1
    return low

# to find the last index <= x
def upper_index(arr, n, x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    return high

def count_in_range(candidate_scores, n, lower_limit, upper_limit):
    return upper_index(candidate_scores, n, upper_limit) - lower_index(candidate_scores, n, lower_limit) + 1
   

def job_offers2(candidate_scores, lower_limits, upper_limits):
    jobs_list = []
    candidate_scores.sort()
    n = len(candidate_scores)
    for i in range(len(lower_limits)):
        jobs_list.append(count_in_range(candidate_scores, n, lower_limits[i], upper_limits[i]))
    return jobs_list



if __name__ == '__main__':
    # candidate_scores = [1, 3, 5, 6, 8]
    # lower_limits = [2]
    # upper_limits = [6]

    candidate_scores = [4, 8, 7]
    lower_limits = [2, 4]
    upper_limits = [8, 4]

    print(job_offers1(candidate_scores, lower_limits, upper_limits))
    print(job_offers2(candidate_scores, lower_limits, upper_limits))


 
# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# Approach:
# Create a dict to map courses with a list of prerequisites --> this is equivalent to adjacency lists
# DFS to check if the created graph does not have a cycle

from collections import defaultdict

def DFS(course, course_dict, taken):
    if not course_dict[course]:
        return True
    if course in taken:
        return False
    taken.add(course)
    for prereq in course_dict[course]:
        if not DFS(prereq, course_dict, taken):
            return False
    course_dict[course] = []
    return True


def canFinish(numCourses, prerequisites):
    # get a list of prerequisites for each course
    course_dict = defaultdict(list)
    for course, prereq in prerequisites:
        course_dict[course].append(prereq)

    taken = set()
    for course in range(numCourses):
        if not DFS(course, course_dict, taken):
            return False
    return True


print(canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(canFinish(numCourses = 2, prerequisites =[[1,0],[0,1]]))
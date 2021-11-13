#Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers and an array where each element indicates the duration of a task.
#We wish to determine the optimal way in which to assign tasks to some workers. Each worker must work on exactly two tasks. Tasks are independent of each other, and each task takes a certain amount of time.

A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
# A group of n students are sitting in a circle. The teacher has to elect a class president.
# The teacher does this by singing a song and going around the circle
# After the song stops, the student at whom the teacher stopped is removed from the circle
# Starting at the student next to the one who was removed, the teacher resumes.
# A song of length k will result in the teacher walking k steps around the circle
# For given n and k, find the last student left in the circle


# Use a circular linked list and simulate the problem

from collections import deque

class CircularLinkedList:
    def __init__(self):
        self.circle = deque()

    def add(self, value):
        self.circle.append(value)

    def add_left(self, value):
        self.circle.appendleft(value)

    def remove(self, value):
        try:
            self.circle.remove(value)
        except ValueError:
            print(f'{value} not found in circular linked list')

    def size(self):
        return len(self.circle)
    
    def get_first(self):
        return list(self.circle)[0]
    
    def display(self):
        print(list(self.circle))


def create_circle(n):
    circle = CircularLinkedList()
    for i in range(1, n + 1):
        circle.add(i)
    return circle          


def who_is_elected(n, k):
    if n == 0:
        return -1
    if n == 1:
        return 1
    
    # create a circular linked list
    circle = create_circle(n)
    print('Start with = ')
    circle.display()
    steps = k

    ptr = 0

    # walk around the circle
    while circle.size() > 1:
        # walk k steps around circle and remove
        while steps > 0:
            ptr += 1
            steps -= 1
        circle.remove(ptr)
        ptr += 1

    return circle.get_first()


test_cases = [[1, 1, 1], [2, 2, 1], [4, 2, 1], [100, 2, 73]]

for test in test_cases:
    n, k, expected = test
    actual = who_is_elected(n, k)
    if actual == expected:
        print(f'Test passed: {test}')
    else:
        print(f'Test failed: {test}, Actual = {actual}, Expected = {expected}')
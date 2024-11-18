# Master Mind: The Game of Master Mind is played as follows:
# The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (G) or
# blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot
# #4 is blue).
# You, the user, are trying to guess the solution. You might, for example, guess YRGB.
# When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists
# but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a
# pseudo-hit.
# For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudohit.
# Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.

from enum import Enum
from collections import defaultdict

class Result:
    def __init__(self):
        self.hits = 0
        self.pseudo_hits = 0

    def print_result(self):
        print(f'Hits = {self.hits}, Pseudo-hits = {self.pseudo_hits}')

class Color(Enum):
    R = 0
    B = 1
    G = 2
    Y = 3


def estimate(guess, solution):
    if len(guess) != len(solution):
        return None
    result = Result()

    freq = defaultdict(int)

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            result.hits += 1
        else:
            code = Color[solution[i]]
            freq[code] += 1

    # compute pseudo-hits
    for i in range(len(guess)):
        code = Color[guess[i]]
        if freq[code] > 0 and guess[i] != solution[i]:
            result.pseudo_hits += 1
            freq[code] -= 1
    
    return result


result = estimate("RGBY", "GGRR")
result.print_result()
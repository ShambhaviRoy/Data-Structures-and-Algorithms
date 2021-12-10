# Given input N and K, an unbiased coin is flipped N times. 
# H = +1, T = -1 on number line traversal
# What is the probability that we'll end up in [-K, K]?
# Constraints: N >= 0, K <= N

import numpy as np

def find_prob(N, K):
    # H = +1, T = -1
    # generate random no. r --> r >= 0.5 (H)
    trials = 2**N
    trial_count = 0
    favorable = 0

    while trial_count < trials:
        flips = 0
        position = 0
        while flips < N:
            r = np.random.rand()
            if r >= 0.5:
                position += 1   # got H
            else:
                position -= 1   # got T
        if np.abs(position) <= K:
            favorable += 1

    return favorable/trials


if __name__ == '__main__':
    print(find_prob(3, 1))
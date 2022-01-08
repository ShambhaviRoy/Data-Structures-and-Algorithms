# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
# Example
# Input s = 'mom'
# The list of all anagrammatic pairs is [['m', 'm'], ['mo', 'om'] at positions [[0], [2]], [[0, 1], [1, 2]] respectively

# Constraints:
# 2 <= len(s) <= 100
# s contains only lowercase letters

#!/bin/python3

import math
import os
import random
import re
import sys


def sherlockAndAnagrams(s):
    # Find substrings
    n = len(s)
    ans = 0
    for i in range(1, n):
        subs_dict = {}
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            print(subs, subs_dict)
            
            # Save substrings in a dict
            if subs not in subs_dict:
                subs_dict[subs] = 1
            else:
                subs_dict[subs] += 1
            
            # Calculate ans
            ans += subs_dict[subs] - 1
            print(subs, subs_dict, ans)
    
    return ans
    
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

        

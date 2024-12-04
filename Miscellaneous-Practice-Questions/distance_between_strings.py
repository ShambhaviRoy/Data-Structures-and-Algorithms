# Find the shortest distance between the midpoints of 2 strings in a document

# Example:
# document = "This is a sample, document. We made up."
# shortest_distance("sample", "we") --> 14

import re

# Time complexity = O(w1 * w2), Space complexity = O(max(w1, w2)), 
# w1 = no. of occurrences of word1 in document, w2 = no. of occurrences of word2 in document

def shortest_distance(document, word1, word2):
    document = document.lower()
    word1 = word1.lower()
    word2 = word2.lower()

    indices1 = [m.start() for m in re.finditer(word1, document)]
    indices2 = [m.start() for m in re.finditer(word2, document)]

    if not indices1 or not indices2:
        return -1

    midpoints1 = [i + len(word1)//2 for i in indices1]
    midpoints2 = [i + len(word2)//2 for i in indices2]

    shortest_dist = float('inf')
    for midpt1 in midpoints1:
        for midpt2 in midpoints2:
            shortest_dist = min(shortest_dist, abs(midpt1 - midpt2))

    return shortest_dist


document = "This is a sample, document. We made up."
print(shortest_distance(document, "sample", "We"))


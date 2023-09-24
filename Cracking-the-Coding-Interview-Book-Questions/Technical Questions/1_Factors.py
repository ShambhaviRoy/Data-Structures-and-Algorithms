# Question: Print all positive integer solutions to the equation a3 + b3 = c3+ d3 where a, b, c and d are integers between 1 and 1000.


# Approach:
# Find sum of cubes of c and d and save them in a dict
# Iterate through the dict to print the pairs
# Time Complexity = O(n^2)



n = 1000
pair_map = {}

for c in range(1, n):
    for d in range(1, n):
        result = c**3 + d**3
        if result not in pair_map:
            pair_map[result] = []
        else:
            if (c, d) not in pair_map[result]:
                pair_map[result].append((c, d))
            


for result, list_pairs in pair_map.items():
    for pair1 in list_pairs:
        for pair2 in list_pairs:
            print(pair1, pair2)
            
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.data = [] 
        self.data_map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        # len(list) = last index + 1
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        
        last = self.data[-1]
        index_of_val = self.data_map[val]

        self.data_map[last] = index_of_val
        
        # swap
        self.data[index_of_val] = last
        self.data[-1] = val
        
        # pop val out of the list and map
        self.data.pop()
        self.data_map.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)

        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
val = 1
param_1 = obj.insert(val)
val = 2
param_2 = obj.remove(val)
param_3 = obj.getRandom()
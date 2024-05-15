# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left


    def insert_node(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev
        

    def remove_node(self, node): 
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]
            
  

lRUCache = LRUCache(2)
print(lRUCache.put(1, 1), lRUCache.cache) # // cache is {1=1}
print(lRUCache.put(2, 2), lRUCache.cache) # // cache is {1=1, 2=2}
print(lRUCache.get(1))#    // return 1
print(lRUCache.put(3, 3), lRUCache.cache)# // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))#   // returns -1 (not found)
print(lRUCache.put(4, 4), lRUCache.cache)# // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))#   // return -1 (not found)
print(lRUCache.get(3))#   // return 3
print(lRUCache.get(4))#    // return 4
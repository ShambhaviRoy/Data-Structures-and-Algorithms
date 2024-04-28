# Hash Table: Design and implement a hash table which uses chaining (linked lists) to handle
# collisions.

class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class Hasher:



    def __init__(self, capacity):
        self.arr = [None] * capacity

    def get(self, key):
        node = self.get_node_for_key(key)
        if node:
            return node.value
        return None


    def put(self, key, value):
        node = self.get_node_for_key(key)
        if not node:
            node.value = value
            return
        node = LinkedListNode(key, value)
        index = self.get_index_for_key(key)
        if(self.arr[index]):
            node.next = self.arr[index]
            node.next.prev = node
        self.arr[index] = node


    def remove(self, key):
        node = self.get_node_for_key(key)
        if node.prev:
            node.prev.next = node.next
        else:
            # remove head
            hash_key = self.get_index_for_key(key)
            self.arr[hash_key] = node.next

        if node.next:
            node.next.prev = node.prev


    def get_node_for_key(self, key):
        index = self.get_index_for_key(key)
        current = self.arr[index]
        while(current):
            if current.key == key:
                return current
            current = current.next
        return None


    def get_index_for_key(self, key):
        return abs(hash(key) % self.arr.size)



# A simple hash table implementation. Handles collisions by overwriting original
# value at location in the hash table. (Could use chaining and linear probing.)

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None]*self.capacity
        self.size = 0

    def is_full(self):
        if self.size == self.capacity:
            return True
        return False
        
    def add_key(self,key,value):
        if self.is_full:
            self.ensure_capacity()
        index = make_hash(key) % self.capacity
        if not self.table[index]:
            self.size += 1
        self.table[index] = value

    def make_hash(self, key):
        hashcode = 1
        for char in key:
            hashcode = hashcode * ord(char)
        index = hashcode % self.capacity
        return index

    def get_value(self,key):
        index = self.make_hash(key)
        if self.table[index] != None:
            return self.table[index]
        raise Exception("Key does not exist.")

    def ensure_capacity(self)
        self.capacity = 2*self.capacity
        old_table = self.table
        self.table = [None]*self.capacity
        for item in old_table:
            if item:
                self.addKey(item, old_table[item])

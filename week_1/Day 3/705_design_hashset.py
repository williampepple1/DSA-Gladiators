# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.number_of_buckets = 2500
        self.set = [[] for _ in range(self.number_of_buckets)]

    def add(self, key: int) -> None:
        bucket = self.getBucket(key)

        if key not in self.set[bucket]:
            self.set[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)

        for idx, val in enumerate(self.set[bucket]):
            if val == key:
                self.set[bucket][idx] = -1
                break

    def contains(self, key: int) -> bool:
        bucket = self.getBucket(key)

        return key in self.set[bucket]

    def getBucket(self, key):
        return key % self.number_of_buckets
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
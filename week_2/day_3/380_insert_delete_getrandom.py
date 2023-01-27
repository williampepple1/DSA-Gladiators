# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []
        self.idx = 0
        
    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False

        self.map[val] = self.idx
        self.arr.append(val)
        self.idx += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        temp = self.arr[-1] #temp  = 9
        idx = self.map[val]
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.map[temp] = idx
        self.idx -= 1
        del self.map[val]
        self.arr.pop()
        return True
    def getRandom(self) -> int:
        rand = math.floor(random.random() * len(self.arr))
        return self.arr[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
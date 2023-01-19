# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_hashmap = {}

        for i, val in enumerate(s):
            if val in my_hashmap:
                my_hashmap[val] += 1
            else:
                my_hashmap[val] = 1
        
        for i, val in enumerate(s):
            if my_hashmap[val] == 1:
                return i
        return -1
        
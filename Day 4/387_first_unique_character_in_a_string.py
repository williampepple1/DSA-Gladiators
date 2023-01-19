# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -2
import 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, num in enumerate(s):
            if count[num] == 1:
                return i
        return -1

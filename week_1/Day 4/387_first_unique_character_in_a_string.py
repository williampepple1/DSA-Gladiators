# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -2

class Solution:
    def firstUniqChar(self, s: str) -> int:

        from collections import Counter
        freq_map = Counter(s)

        for index, char in enumerate(s):
            if freq_map[char] == 1:
                return index
        
        return -1
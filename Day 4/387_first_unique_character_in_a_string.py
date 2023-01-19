# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        from collections import Counter
        cntr = Counter(s)
        for idx, ltr in enumerate(s):
            if cntr.get(ltr) == 1:
                return idx
        return -2

    """
    Time - O(n)
    Space - O(n)
    """

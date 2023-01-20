# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    substringSet = set()
        l = 0
        length = 0
        for r in range(0, len(s)):
            while s[r] in substringSet:
                substringSet.remove(s[l])
                l += 1
            substringSet.add(s[r])
            length = max(length, r - l + 1)
        return length

    """
    Time - O(n)
    Space - O(n)
    """
        
